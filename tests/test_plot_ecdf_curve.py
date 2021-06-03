import pytest
import pandas as pd
from galeritas import plot_ecdf_curve


@pytest.fixture(scope='module')
def load_data():
    data = pd.read_csv("tests/data/titanic.csv")

    return data


@pytest.mark.mpl_image_compare
def test_should_generate_plot_correctly(load_data):
    df = load_data

    return plot_ecdf_curve(
        df=df,
        column_to_plot='fare',
        hue='pclass',
        plot_title='Fare distribution by PClass',
        figsize=(16, 6),
        percentiles=(25, 50, 75, 90),
        mark_percentiles=True
    )


def test_should_return_figure_with_axes_ecdf(load_data):
    df = load_data

    fig = plot_ecdf_curve(
        df=df,
        column_to_plot='fare',
        hue='pclass',
        plot_title='Fare distribution by PClass',
        figsize=(16, 6),
        percentiles=(25, 50, 75, 90),
        mark_percentiles=True
    )

    assert fig.get_axes() is not None


def test_should_raise_warning_about_missing_values(load_data):
    df = load_data

    with pytest.warns(UserWarning):
        plot_ecdf_curve(
            df=df,
            column_to_plot='age'
        )

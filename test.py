import marimo

__generated_with = "0.14.13"
app = marimo.App()


@app.cell
def _():
    1 + 3
    return


if __name__ == "__main__":
    app.run()

import gradio
import pytest

from grompy.transpiler import TranspilerError, transpile


def test_basic_arithmetic_without_type_hints():
    def simple_add(a, b):
        return a + b

    with pytest.raises(TranspilerError) as e:
        transpile(simple_add)

    assert "Line 2" in str(e.value)


def test_basic_arithmetic_with_type_hints():
    def simple_add(a: int, b: int):
        return a + b

    expected = """function simple_add(a, b) {
    return (a + b);
}"""
    assert transpile(simple_add).strip() == expected.strip()


def test_if_else():
    def check_value(x: int):
        if x > 10:
            return "high"
        else:
            return "low"

    expected = """function check_value(x) {
    if ((x > 10)) {
        return 'high';
    }
    else {
        return 'low';
    }
}"""
    assert transpile(check_value).strip() == expected.strip()


def test_variable_assignment():
    def assign_vars(x: int):
        y = x * 2
        z = y + 1
        return z

    expected = """function assign_vars(x) {
    let y = (x * 2);
    let z = (y + 1);
    return z;
}"""
    assert transpile(assign_vars).strip() == expected.strip()


def test_for_loop_range():
    def sum_range(n: int):
        total = 0
        for i in range(n):
            total = total + i
        return total

    expected = """function sum_range(n) {
    let total = 0;
    for (let i of Array.from({length: n}, (_, i) => i)) {
        total = (total + i);
    }
    return total;
}"""
    assert transpile(sum_range).strip() == expected.strip()


def test_while_loop():
    def countdown(n: int):
        while n > 0:
            n = n - 1
        return n

    expected = """function countdown(n) {
    while ((n > 0)) {
        let n = (n - 1);
    }
    return n;
}"""
    assert transpile(countdown).strip() == expected.strip()


def test_list_operations():
    def make_list(x: int):
        arr = [1, 2, x]
        arr[0] = x
        return arr

    expected = """function make_list(x) {
    let arr = [1, 2, x];
    arr[0] = x;
    return arr;
}"""
    assert transpile(make_list).strip() == expected.strip()


def test_comparison_operators():
    def compare_values(a: int, b: int):
        if a == b:
            return "equal"
        elif a > b:
            return "greater"
        else:
            return "less"

    expected = """function compare_values(a, b) {
    if ((a === b)) {
        return 'equal';
    }
    else if ((a > b)) {
        return 'greater';
    }
    else {
        return 'less';
    }
}"""
    assert transpile(compare_values).strip() == expected.strip()


def test_boolean_operations():
    def logical_ops(a: bool, b: bool):
        return a and b or not a

    with pytest.raises(TranspilerError) as e:
        transpile(logical_ops)

    assert "Line 2" in str(e.value)


def test_dict_operations():
    def create_dict(key, value):
        d = {"fixed": 42, key: value}
        return d

    expected = """function create_dict(key, value) {
    let d = {'fixed': 42, key: value};
    return d;
}"""
    assert transpile(create_dict).strip() == expected.strip()


def test_simple_lambda():
    simple_lambda = lambda x: x  # noqa: E731

    expected = """function (x) {
    return x;
}"""
    assert transpile(simple_lambda).strip() == expected.strip()


def test_multi_param_lambda_with_None():
    multi_param = lambda x, y: None  # noqa: E731

    expected = """function (x, y) {
    return null;
}"""
    assert transpile(multi_param).strip() == expected.strip()


def test_multiple_return_values():
    def return_multiple(x: int, y: int):
        return x, y, x + y

    expected = """function return_multiple(x, y) {
    return [x, y, (x + y)];
}"""
    assert transpile(return_multiple).strip() == expected.strip()


def test_single_gradio_component():
    def create_textbox():
        return gradio.Textbox(lines=8, visible=True, value="Lorem ipsum")

    expected = """function create_textbox() {
    return {"lines": 8, "visible": true, "value": "Lorem ipsum", "__type__": "update"};
}"""
    assert transpile(create_textbox).strip() == expected.strip()


def test_multiple_gradio_components():
    def create_interface():
        text_input = gradio.Textbox(label="Input", lines=2)
        button = gradio.Button(value="Submit", interactive=True)
        output = gradio.Textbox(label="Output")
        return text_input, button, output

    expected = """function create_interface() {
    let text_input = {"label": "Input", "lines": 2, "__type__": "update"};
    let button = {"value": "Submit", "interactive": true, "__type__": "update"};
    let output = {"label": "Output", "__type__": "update"};
    return [text_input, button, output];
}"""
    assert transpile(create_interface).strip() == expected.strip()


def test_len_function():
    def get_length(arr: list, dictionary: dict):
        return len(arr), len(dictionary)

    expected = """function get_length(arr, dictionary) {
    return [arr.length, Object.keys(dictionary).length];
}"""
    assert transpile(get_length).strip() == expected.strip()


def test_list_comprehension_with_in():
    def filter_rows_by_term(data: list, search_term: str) -> list:
        return [row for row in data if search_term in row[0]]

    expected = """function filter_rows_by_term(data, search_term) {
    return data.filter(row => row[0].includes(search_term));
}"""
    assert transpile(filter_rows_by_term).strip() == expected.strip()

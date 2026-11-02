# gui.py

import core.case_tools as case_tools
import core.cleaner_tools as cleaner_tools
import core.developer_tools as developer_tools

import tkinter as tk
from tkinter import ttk


def main():
    root = tk.Tk()
    root.title("Text Toolbox")

    window_width = 800
    window_height = 600

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    root.geometry(
        f"{window_width}x{window_height}+{x}+{y}"
    )
    root.minsize(800, 600)

    # Main layout
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    main_frame = ttk.Frame(root, padding=10)
    main_frame.grid(row=0, column=0, sticky="nsew")
    main_frame.columnconfigure(0, weight=1)
    main_frame.columnconfigure(1, weight=1)
    main_frame.rowconfigure(0, weight=1)

    # Input area
    input_frame = ttk.LabelFrame(
        main_frame, text="Input", padding=5
    )
    input_frame.grid(
        row=0, column=0, sticky="nsew", padx=(0, 5)
    )
    input_frame.rowconfigure(0, weight=1)
    input_frame.columnconfigure(0, weight=1)

    input_text = tk.Text(input_frame, wrap="word")
    input_text.grid(row=0, column=0, sticky="nsew")

    input_scrollbar = ttk.Scrollbar(
        input_frame,
        orient="vertical",
        command=input_text.yview,
    )
    input_scrollbar.grid(row=0, column=1, sticky="ns")
    input_text.configure(yscrollcommand=input_scrollbar.set)

    # Output area
    output_frame = ttk.LabelFrame(
        main_frame, text="Output", padding=5
    )
    output_frame.grid(
        row=0, column=1, sticky="nsew", padx=(5, 0)
    )
    output_frame.rowconfigure(0, weight=1)
    output_frame.columnconfigure(0, weight=1)

    output_text = tk.Text(output_frame, wrap="word")
    output_text.grid(row=0, column=0, sticky="nsew")

    output_scrollbar = ttk.Scrollbar(
        output_frame,
        orient="vertical",
        command=output_text.yview,
    )
    output_scrollbar.grid(row=0, column=1, sticky="ns")
    output_text.configure(yscrollcommand=output_scrollbar.set)

    # Helper function for text conversion (inside main to access widgets & update_stats)
    def update_stats():
        inp_text = input_text.get("1.0", "end-1c")
        out_text = output_text.get("1.0", "end-1c")

        inp_chars = len(inp_text)
        inp_words = len(inp_text.split()) if inp_text.strip() else 0
        inp_lines = len(inp_text.splitlines()) if inp_text else 0

        out_chars = len(out_text)
        out_words = len(out_text.split()) if out_text.strip() else 0
        out_lines = len(out_text.splitlines()) if out_text else 0

        w_chars = max(len(str(inp_chars)), len(str(out_chars)), 1)
        w_words = max(len(str(inp_words)), len(str(out_words)), 1)
        w_lines = max(len(str(inp_lines)), len(str(out_lines)), 1)

        input_stats_var.set(
            f" Input: {inp_chars:>{w_chars}} chars | {inp_words:>{w_words}} words | {inp_lines:>{w_lines}} lines"
        )
        output_stats_var.set(
            f"Output: {out_chars:>{w_chars}} chars | {out_words:>{w_words}} words | {out_lines:>{w_lines}} lines"
        )

    def convert_text(converter):
        text = input_text.get("1.0", "end-1c")
        result = converter(text)

        output_text.delete("1.0", tk.END)
        output_text.insert("1.0", result)
        update_stats()  # Automatically update stats when output changes!

    # Case conversion button definitions
    case_button_definitions = [
        ("UPPERCASE", case_tools.to_uppercase),
        ("lowercase", case_tools.to_lowercase),
        ("Title Case", case_tools.to_title_case),
        ("Sentence Case", case_tools.to_sentence_case),
        ("Invert Case", case_tools.invert_case),
    ]

    # Text cleaning button definitions
    cleaning_button_definitions = [
        ("Remove Leading/Trailing Spaces", cleaner_tools.remove_leading_trailing_spaces),
        ("Remove Extra Spaces", cleaner_tools.remove_extra_spaces),
        ("Remove Blank Lines", cleaner_tools.remove_blank_lines),
        ("Remove Duplicate Lines", cleaner_tools.remove_duplicate_lines),
        ("Remove Special Characters", cleaner_tools.remove_special_characters),
        ("Remove Digits", cleaner_tools.remove_digits),
        ("Remove Tabs", cleaner_tools.remove_tabs),
        ("Normalize to ASCII", cleaner_tools.normalize_to_ascii),
    ]

    # Developer Tools button definitions (Grouped encode/decode pairs)
    developer_button_definitions = [
        ("Minify Python Code", developer_tools.minify_python_code),
        ("Base64 Encode", developer_tools.base64_encode),
        ("Base64 Decode", developer_tools.base64_decode),
        ("Format JSON", developer_tools.format_json),
        ("URL Encode", developer_tools.url_encode),
        ("URL Decode", developer_tools.url_decode),
    ]

    # Button state management
    def update_button_states(event=None):
        input_text.edit_modified(False)

        has_text = bool(
            input_text.get("1.0", "end-1c").strip()
        )
        state = "normal" if has_text else "disabled"

        for button in case_buttons + cleaning_buttons + developer_buttons:
            button.configure(state=state)

        line_ending_dropdown.configure(
            state="readonly" if has_text else "disabled"
        )
        update_stats()

    # Case conversion buttons
    case_frame = ttk.LabelFrame(
        main_frame, text="Case Conversion", padding=5
    )
    case_frame.grid(
        row=1, column=0, columnspan=2,
        sticky="ew", pady=(10, 0)
    )

    case_buttons = []

    for column, (label, converter) in enumerate(
        case_button_definitions
    ):
        button = ttk.Button(
            case_frame,
            text=label,
            command=lambda func=converter: convert_text(func),
        )
        button.grid(row=0, column=column, padx=5, pady=5, sticky="ew")
        case_frame.columnconfigure(column, weight=1)
        case_buttons.append(button)

    # Text cleaning buttons
    cleaning_frame = ttk.LabelFrame(
        main_frame, text="Text Cleaning", padding=5
    )
    cleaning_frame.grid(
        row=2, column=0, columnspan=2,
        sticky="ew", pady=(10, 0)
    )

    for i in range(4):
        cleaning_frame.columnconfigure(i, weight=1)

    cleaning_buttons = []

    for index, (label, cleaner) in enumerate(
        cleaning_button_definitions
    ):
        button = ttk.Button(
            cleaning_frame,
            text=label,
            command=lambda func=cleaner: convert_text(func),
        )

        row = index // 4
        column = index % 4

        button.grid(
            row=row, column=column, padx=5, pady=5, sticky="ew"
        )
        cleaning_buttons.append(button)

    # Line-ending controls
    line_ending_style = tk.StringVar(value="windows")

    ttk.Label(
        cleaning_frame,
        text="Line Endings:",
    ).grid(
        row=2, column=0, padx=5, pady=5, sticky="e"
    )

    line_ending_dropdown = ttk.Combobox(
        cleaning_frame,
        textvariable=line_ending_style,
        values=("windows", "unix", "mac"),
        state="readonly",
        width=10,
    )
    line_ending_dropdown.grid(
        row=2, column=1, padx=5, pady=5, sticky="ew"
    )

    normalize_line_endings_button = ttk.Button(
        cleaning_frame,
        text="Normalize Line Endings",
        command=lambda: convert_text(
            lambda text: cleaner_tools.normalize_line_endings(
                text, line_ending_style.get()
            )
        ),
    )
    normalize_line_endings_button.grid(
        row=2, column=2, columnspan=2, padx=5, pady=5, sticky="ew"
    )
    cleaning_buttons.append(normalize_line_endings_button)

    # Developer Tools frame
    developer_frame = ttk.LabelFrame(
        main_frame, text="Developer Tools", padding=5
    )
    developer_frame.grid(
        row=3, column=0, columnspan=2,
        sticky="ew", pady=(10, 0)
    )

    for i in range(3):
        developer_frame.columnconfigure(i, weight=1)

    developer_buttons = []

    for index, (label, func) in enumerate(
        developer_button_definitions
    ):
        button = ttk.Button(
            developer_frame,
            text=label,
            command=lambda f=func: convert_text(f),
        )

        row = index // 3
        column = index % 3

        button.grid(
            row=row, column=column, padx=5, pady=5, sticky="ew"
        )
        developer_buttons.append(button)

    # Bottom Action & Stats Frame (Row 4)
    action_frame = ttk.Frame(main_frame)
    action_frame.grid(
        row=4, column=0, columnspan=2,
        sticky="ew", pady=(10, 0)
    )
    action_frame.columnconfigure(0, weight=1)
    action_frame.columnconfigure(1, weight=0)

    # Left side: Live Stats Labels (Using Consolas monospaced font)
    stats_frame = ttk.Frame(action_frame)
    stats_frame.grid(row=0, column=0, sticky="w")

    input_stats_var = tk.StringVar(value=" Input: 0 chars | 0 words | 0 lines")
    output_stats_var = tk.StringVar(value="Output: 0 chars | 0 words | 0 lines")

    ttk.Label(stats_frame, textvariable=input_stats_var, font=("Consolas", 9)).grid(row=0, column=0, sticky="w")
    ttk.Label(stats_frame, textvariable=output_stats_var, font=("Consolas", 9)).grid(row=1, column=0, sticky="w")

    # Monitor changes in the Input area
    input_text.bind(
        "<<Modified>>", update_button_states
    )
    input_text.edit_modified(False)
    update_stats()

    # Output actions & Selection commands
    def select_input():
        input_text.tag_add(tk.SEL, "1.0", tk.END)
        input_text.mark_set(tk.INSERT, "1.0")
        input_text.see(tk.INSERT)
        input_text.focus_set()

    def select_output():
        output_text.tag_add(tk.SEL, "1.0", tk.END)
        output_text.mark_set(tk.INSERT, "1.0")
        output_text.see(tk.INSERT)
        output_text.focus_set()

    def copy_output():
        text = output_text.get("1.0", "end-1c")
        root.clipboard_clear()
        root.clipboard_append(text)

    def replace_input():
        text = output_text.get("1.0", "end-1c")
        input_text.delete("1.0", tk.END)
        input_text.insert("1.0", text)
        update_stats()

    def clear_text():
        input_text.delete("1.0", tk.END)
        output_text.delete("1.0", tk.END)
        input_text.focus_set()
        update_stats()

    # Right side: Action Buttons
    buttons_subframe = ttk.Frame(action_frame)
    buttons_subframe.grid(row=0, column=1, sticky="e")

    ttk.Button(buttons_subframe, text="Select Input", command=select_input).grid(row=0, column=0, padx=3)
    ttk.Button(buttons_subframe, text="Select Output", command=select_output).grid(row=0, column=1, padx=3)
    ttk.Button(buttons_subframe, text="Copy Output", command=copy_output).grid(row=0, column=2, padx=3)
    ttk.Button(buttons_subframe, text="Replace Input", command=replace_input).grid(row=0, column=3, padx=3)
    ttk.Button(buttons_subframe, text="Clear", command=clear_text).grid(row=0, column=4, padx=3)
    ttk.Button(buttons_subframe, text="Exit", command=root.destroy).grid(row=0, column=5, padx=(3, 0))

    root.mainloop()


if __name__ == "__main__":
    main()

import reflex as rx


class htmlState(rx.State):
    code: str

    rx.event
    def update_code(self, new_code: str):
        self.code = new_code


def html_render(code: str):
    htmlState.code = code
    return rx.container(
        rx.dialog.close(
            rx.button("Close", size="2"),
            position="sticky",
            top="0",
            left="0",
        ),
        rx.container(
            rx.heading(
                "HTML Component",
                align="center",
                justify="center",
                margin_bottom="10px",
            ),
            # rx.spacer(spacing="8"),
            rx.desktop_only(
                rx.hstack(
                    # rx.scroll_area(
                    #     rx.text_area(
                    #         on_change=htmlState.update_code,
                    #         value=htmlState.code,
                    #         style={"height": "60vh", "width": "90vh"},
                    #         # border_radius="1em",
                    #     ),
                    #     type="always",
                    #     scrollbars="both",
                    #     border_radius=".2em",
                    # ),
                    rx.code_block(
                        htmlState.code,
                        show_line_numbers=True,
                        can_copy=True,
                        wrap_long_lines=True,  
                        style={"height": "60vh", "width": "50vh"},
                        # padding="6px",
                    ),
                    rx.spacer(spacing="2"),
                    rx.el.iframe(
                        src_doc=htmlState.code,
                        style={"height": "60vh", "width": "50vh"},
                        # border_radius="1em",
                    ),
                ),
            ),
            rx.mobile_and_tablet(
                rx.vstack(
                    # rx.spacer(spacing="1"),
                    rx.el.iframe(
                        src_doc=htmlState.code,
                        style={"height": "35vh", "width": "25vh"},
                        border_radius=".5em",
                    ),
                    # rx.scroll_area(
                    #     rx.text_area(
                    #         on_change=htmlState.update_code,
                    #         value=htmlState.code,
                    #         style={"height": "35vh", "width": "25vh"},
                    #         # border_radius="1em",
                    #     ),
                    #     type="always",
                    #     scrollbars="both",
                    #     border_radius=".2em",
                    # ),
                    rx.code_block(
                        htmlState.code,
                        show_line_numbers=True,
                        can_copy=True,
                        wrap_long_lines=True,  
                        style={"height": "35vh", "width": "25vh"},
                        # padding="6px",
                    ),
                    rx.spacer(spacing="2"),
                    justify="center",
                    align="center",
                    # min_width="60vh"
                ),
                # rx.spacer(spacing="2"),
            ),
        ),
        code=code,
        id="jamestitus",
        # scope=react()
        # reactRunner(code=code)
    )
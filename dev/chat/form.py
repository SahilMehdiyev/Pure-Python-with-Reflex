import reflex as rx

from .state import ChatState



def chat_form() -> rx.Component:

    return rx.form(
        rx.vstack(
            rx.text_area(
                name = 'message',
                placeholder = 'Your message',
                required=True,
                width ='100%',
            ),
            rx.hstack(
                rx.button('Submit',type='submit'),
                rx.cond(
                    ChatState.did_submit,
                    rx.text('Submitted'),
                    rx.text('Did not submit')
                )
            )
        ),

        on_submit = ChatState.handle_submit,
        reset_on_submit = True
    )
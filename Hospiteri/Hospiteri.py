"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config





meta = [
    {"name": "theme_color", "content": "#FFFFFF"},
    {"char_set": "UTF-8"},
    {"property": "og:url", "content": "url"},
]




@rx.page(
    title="My Beautiful App",
    description="A beautiful app built with Reflex",
    image="/splash.png",
    meta=meta,
)



@rx.page(title="About Page")
def about():
    return rx.text("About Page")


class State(rx.State):
    """The app state."""
    authenticated: bool

    def check_auth(self):
        # Check if user is authenticated
        self.authenticated = check_auth()
        if not self.authenticated:
            return rx.redirect("/login")
    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )

def login() -> rx.Component:
    return rx.grid(
        rx.color_mode.button(position="top-right"),
    rx.card(
        rx.vstack(
            rx.center(
                rx.image(
                    src=rx.color_mode_cond(
                            light="/logo_light.webp",
                            dark="/logo_dark.webp"
                            ),
                    width="24vh",
                    height="auto",
                    border_radius="15%",
                ),
                rx.heading(
                    "Welcome Back! Login Below",
                    size="7",
                    as_="h2",
                    text_align="center",
                    width="100%",
                ),
                direction="column",
                spacing="5",
                width="100%",
            ),
            rx.vstack(
                rx.text(
                    "Email address",
                    size="3",
                    weight="medium",
                    text_align="left",
                    width="100%",
                ),
                rx.input(
                    rx.input.slot(rx.icon("user")),
                    placeholder="user@reflex.dev",
                    type="email",
                    size="3",
                    width="100%",
                ),
                spacing="2",
                width="100%",
            ),
            rx.vstack(
                rx.hstack(
                    rx.text(
                        "Password",
                        size="3",
                        weight="medium",
                    ),
                    rx.link(
                        "Forgot password?",
                        href="#",
                        size="3",
                    ),
                    justify="between",
                    width="100%",
                ),
                rx.input(
                    rx.input.slot(rx.icon("lock")),
                    placeholder="Enter your password",
                    type="password",
                    size="3",
                    width="100%",
                ),
                spacing="2",
                width="100%",
            ),
            rx.button("Login", size="3", width="100%"),
            rx.center(
                rx.text("New here?", size="3"),
                rx.link("Sign up", href="/signup", size="3"),
                opacity="0.8",
                spacing="2",
                direction="row",
                width="100%",
            ),
            spacing="6",
            width="100%",
        ),
        max_width="34em",
        size="4",
        display='grid',
        placeItems='center',
        width="100%",
        backgroundColor=rx.color_mode_cond(light='#e1f1ff',dark='#18191b')    
    ),
    placeItems='center',
    width='100%',
    minHeight='100vh'
    )

def signup() -> rx.Component:
    return rx.grid(
        rx.color_mode.button(position="top-right"),
    rx.card(
            rx.vstack(
                rx.center(
                    rx.image(
                        src=rx.color_mode_cond(
                            light="/logo_light.webp",
                            dark="/logo_dark.webp"
                            ),
                        width="24vh",
                        height="auto",
                        borderRadius="10%",
                    ),
                    rx.heading(
                        "Create an account",
                        size="6",
                        as_="h2",
                        text_align="center",
                        width="100%",
                    ),
                    direction="column",
                    spacing="5",
                    width="100%",
                ),
                rx.vstack(
                    rx.text(
                        "Email address",
                        size="3",
                        weight="medium",
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        rx.input.slot(rx.icon("user")),
                        placeholder="user@reflex.dev",
                        type="email",
                        size="3",
                        width="100%",
                    ),
                    justify="start",
                    spacing="2",
                    width="100%",
                ),
                rx.vstack(
                    rx.text(
                        "Password",
                        size="3",
                        weight="medium",
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        rx.input.slot(rx.icon("lock")),
                        placeholder="Enter your password",
                        type="password",
                        size="3",
                        width="100%",
                    ),
                    justify="start",
                    spacing="2",
                    width="100%",
                ),
                rx.box(
                    rx.checkbox(
                        "Agree to Terms and Conditions",
                        default_checked=True,
                        spacing="2",
                    ),
                    width="100%",
                ),
                rx.button("Sign in", size="3", width="100%"),
                rx.center(
                    rx.text("Already registered?", size="3"),
                    rx.link("Sign in", href="#", size="3"),
                    opacity="0.8",
                    spacing="2",
                    direction="row",
                    width="100%",
                ),
                spacing="6",
                width="100%",
            ),
            max_width="28em",
            size="4",
            width="100%",
            backgroundColor=rx.color_mode_cond(light='#e1f1ff',dark='#18191b')    
    
        ),
    placeItems='center',
    width='100%',
    minHeight='100vh'
    )




app = rx.App()
app.add_page(about)
app.add_page(index)
app.add_page(login)
app.add_page(signup)

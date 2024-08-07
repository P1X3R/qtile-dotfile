from libqtile import bar, widget
from libqtile.config import Screen

def separator(fore: str, back: str | None):
    return widget.TextBox(
        foreground=fore,
        background=back,
        text="", # Icon: nf-oct-triangle_left
        fontsize=95,
        padding=-22
    )

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(text=" "),
                widget.CurrentLayout(foreground="#e06c75"),
                widget.GroupBox(active="#98c479", inactive="#abb2bf", rounded=False, highlight_method="line", urgent_alert_method="text", padding_x=5, padding_y=10, this_current_screen_border="#61afef"),
                # widget.Prompt(),
                widget.WindowName(foreground="#c678dd"),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),

                widget.Systray(),
                widget.TextBox(text=" ", fontsize=4),
                separator(fore="#e5c07b", back=None),
                widget.TextBox(text="󱑋", fontsize=20, background="#e5c07b", foreground="#282c34"), # Clock Icon
                widget.Clock(format="%I:%M %p ", background="#e5c07b", foreground="#282c34"),

                separator(fore="#61afef", back="#e5c07b"),
                widget.TextBox(text="󰭧", fontsize=20, background="#61afef", foreground="#282c34"), # Clock Icon
                widget.Clock(format="%a %Y / %m / %d ", background="#61afef", foreground="#282c34"),
            ],
            24,
            background="#282c34",
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]


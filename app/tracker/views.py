from django.shortcuts import render


def get_html_path(request, fpath, fname):
    if request.htmx:
        return f"{fpath}/{fname}.html"
    return f"{fpath}/{fname}_extends.html"


def dashboard_view(request):
    html_file = get_html_path(request, "main", "dashboard")
    return render(request, html_file)

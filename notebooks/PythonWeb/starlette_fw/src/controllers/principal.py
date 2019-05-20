from ..settings import templates


def documentation(request):
    return templates.TemplateResponse("app/index.html", {"request": request})

from operator import itemgetter
import requests
import plotly.express as px

# Make an API call and check the response
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:5]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article
    submission_dict = {
        "title": response_dict["title"][:50],  # Limitar longitud del título
        "hn_link": f"https://news.ycombinator.com/item?id={submission_id}",
        "comments": response_dict.get("descendants", 0),  # Usar get para evitar errores
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter("comments"), reverse=True)

# Preparar datos para la gráfica
titles = [f"<a href='{d['hn_link']}'>{d['title']}</a>" for d in submission_dicts]
comments = [d["comments"] for d in submission_dicts]
hover_texts = [f"Enlace: {d['hn_link']}" for d in submission_dicts]

# Crear la gráfica
fig = px.bar(
    x=titles,
    y=comments,
    title="Discusiones más activas en Hacker News",
    labels={"x": "Historia", "y": "Número de comentarios"},
    hover_name=hover_texts
)

# Personalizar la gráfica
fig.update_layout(
    title_font_size=28,
    xaxis_title_font_size=20,
    yaxis_title_font_size=20
)
fig.update_traces(
    marker_color="SteelBlue",
    marker_opacity=0.6,
    text=comments,  # Mostrar número de comentarios en las barras
    textposition="auto"
)

# Guardar la gráfica como archivo HTML
fig.show()
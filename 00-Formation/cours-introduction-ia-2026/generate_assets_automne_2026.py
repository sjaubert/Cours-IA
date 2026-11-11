"""
Diagrammes de la séquence « Automne 2026 : IA et démonstrations mathématiques »
(diapositives 73 à 75 et 82 du diaporama d'Introduction à l'IA).

Même charte que generate_light_assets.py : fond blanc, DejaVu Sans, palette ardoise.
État des faits : 11 novembre 2026. À revérifier avant chaque session.
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
os.makedirs(OUTPUT_DIR, exist_ok=True)

plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.family'] = 'sans-serif'

INK, MUTED, BODY, PANEL = '#0F172A', '#475569', '#334155', '#F8FAFC'
BLUE, DEEP, GREEN, RED, AMBER, GREY = '#0284C7', '#2563EB', '#16A34A', '#DC2626', '#D97706', '#CBD5E1'
FIGSIZE = (12, 7.5)  # ratio 1,6 : identique aux autres diagrammes du diaporama


def new_fig(title, subtitle):
    fig = plt.figure(figsize=FIGSIZE, facecolor='#FFFFFF')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.text(0.5, 0.94, title, fontsize=15, fontweight='bold', ha='center', va='center', color=INK)
    ax.text(0.5, 0.885, subtitle, fontsize=11, ha='center', va='center', color=MUTED)
    return fig, ax


def card(ax, x, y, w, h, edge, face=PANEL, lw=2):
    ax.add_patch(patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.008,rounding_size=0.02",
                                        facecolor=face, edgecolor=edge, linewidth=lw))


def save(fig, name):
    fig.savefig(os.path.join(OUTPUT_DIR, name), dpi=250, facecolor='#FFFFFF')
    plt.close(fig)


def generate_timeline():
    fig, ax = new_fig("AUTOMNE 2026 : L'IA PRODUIT DES DÉMONSTRATIONS MATHÉMATIQUES",
                      "Quatre dates en sept semaines")
    y0, x_min, x_max = 0.49, 0.07, 0.93

    def xpos(day):  # jour 0 = 1er septembre, jour 75 = 15 novembre
        return x_min + (x_max - x_min) * day / 75

    ax.plot([x_min, x_max], [y0, y0], color=GREY, lw=4, solid_capstyle='round', zorder=1)
    for day, label in [(0, "1er sept."), (30, "1er oct."), (61, "1er nov.")]:
        ax.plot([xpos(day)] * 2, [y0 - 0.012, y0 + 0.012], color=MUTED, lw=1.5, zorder=2)
        ax.text(xpos(day), y0 - 0.035, label, fontsize=9, ha='center', va='top', color=MUTED)

    events = [
        # jour, centre x de la carte, haut ?, couleur, date, titre, détail
        (7, 0.185, True, BLUE, "8 septembre", "OpenAI : Navier-Stokes",
         "Variante avec force extérieure\n10 000 agents IA, 88 heures"),
        (10, 0.26, False, AMBER, "11 septembre", "25 médaillés Fields",
         "Déclaration publique :\nla compréhension avant la vitesse"),
        (35, 0.50, True, BLUE, "6 octobre", "OpenAI : 722 manuscrits",
         "Publiés en une fois\n3 retraits dès le lendemain"),
        (55.5, 0.745, False, DEEP, "26 et 27 octobre", "OpenAI puis Anthropic",
         "Réfutation annoncée de\nl'Exponential Time Hypothesis"),
    ]
    w, h = 0.27, 0.215
    for day, cx, top, col, date, title, detail in events:
        x = xpos(day)
        y_card = y0 + 0.075 if top else y0 - 0.075 - h
        y_edge = y_card if top else y_card + h
        ax.plot([x, x], [y0, y_edge], color=col, lw=2, zorder=2)
        ax.scatter([x], [y0], s=170, color=col, edgecolor='#FFFFFF', linewidth=2, zorder=3)
        card(ax, cx - w / 2, y_card, w, h, col)
        ax.text(cx, y_card + h - 0.038, date, fontsize=11, fontweight='bold', ha='center', va='center', color=col)
        ax.text(cx, y_card + h - 0.085, title, fontsize=12, fontweight='bold', ha='center', va='center', color=INK)
        ax.text(cx, y_card + 0.058, detail, fontsize=10, ha='center', va='center', color=BODY, linespacing=1.4)

    xs = xpos(71)
    ax.plot([xs, xs], [y0, y0 + 0.075], color=MUTED, lw=2, ls=(0, (3, 2)), zorder=2)
    ax.scatter([xs], [y0], s=170, color='#FFFFFF', edgecolor=MUTED, linewidth=2.5, zorder=3)
    card(ax, 0.775, y0 + 0.075, 0.2, 0.15, MUTED, face='#FFFFFF')
    ax.text(0.875, y0 + 0.185, "11 novembre", fontsize=10.5, fontweight='bold', ha='center', va='center', color=MUTED)
    ax.text(0.875, y0 + 0.125, "Relectures humaines\nen cours", fontsize=9.5, ha='center', va='center',
            color=BODY, linespacing=1.4)

    card(ax, 0.07, 0.035, 0.86, 0.075, GREY, lw=1.5)
    ax.text(0.5, 0.0725, "Annonces d'entreprises. Aucune n'est passée par une revue à comité de lecture au 11 novembre 2026.",
            fontsize=10.5, ha='center', va='center', color=INK)
    save(fig, "automne_2026_chronologie.png")


def generate_status_matrix():
    fig, ax = new_fig("REVENDIQUÉ, VÉRIFIÉ PAR MACHINE, VALIDÉ PAR DES HUMAINS",
                      "Trois niveaux de preuve à ne pas confondre (état au 11 novembre 2026)")
    col_x = [0.035, 0.345, 0.505, 0.745]
    col_w = [0.28, 0.13, 0.21, 0.215]
    heads = ["Résultat annoncé", "Revendiqué", "Vérifié par machine\n(assistant de preuve Lean)",
             "Validé par des humains\n(relecture par les pairs)"]
    y_head, h_head = 0.735, 0.095
    for x, w, t in zip(col_x, col_w, heads):
        card(ax, x, y_head, w, h_head, INK, face=INK, lw=1)
        ax.text(x + w / 2, y_head + h_head / 2, t, fontsize=10, fontweight='bold', ha='center', va='center',
                color='#FFFFFF', linespacing=1.35)

    ok, mid, ko = (GREEN, '#F0FDF4'), (AMBER, '#FFFBEB'), (RED, '#FEF2F2')
    rows = [
        ("Navier-Stokes", "8 sept. Variante avec force extérieure",
         ("Oui", ok), ("Oui, mais l'énoncé\nvérifié est contesté", mid), ("Non", ko)),
        ("722 manuscrits", "6 oct. 372 familles de résultats",
         ("Oui", ok), ("Environ 42 %", mid), ("Aucune revue\npar les pairs", ko)),
        ("Zéros de la fonction zêta", "6 oct. Aucun zéro au-delà de 7/8",
         ("Oui", ok), ("Oui", ok), ("Jugé largement correct\npar des spécialistes", mid)),
        ("Réfutation de l'ETH", "26 et 27 oct. OpenAI et Anthropic",
         ("Oui", ok), ("Oui, preuve écrite et\nrelue par des IA", mid), ("Relecture en cours,\nsans verdict", mid)),
    ]
    h_row, gap = 0.125, 0.02
    for i, (name, sub, *cells) in enumerate(rows):
        y = y_head - (i + 1) * (h_row + gap)
        card(ax, col_x[0], y, col_w[0], h_row, GREY, lw=1.5)
        ax.text(col_x[0] + 0.018, y + h_row * 0.64, name, fontsize=11, fontweight='bold', ha='left', va='center', color=INK)
        ax.text(col_x[0] + 0.018, y + h_row * 0.3, sub, fontsize=9.3, ha='left', va='center', color=MUTED)
        for x, w, (txt, (edge, face)) in zip(col_x[1:], col_w[1:], cells):
            card(ax, x, y, w, h_row, edge, face=face)
            ax.text(x + w / 2, y + h_row / 2, txt, fontsize=10.5, fontweight='bold', ha='center', va='center',
                    color=edge, linespacing=1.35)

    ax.text(0.5, 0.062, "Lean contrôle que chaque étape découle de l'énoncé fourni. Il ne dit pas si cet énoncé est le bon.",
            fontsize=10.5, ha='center', va='center', color=INK, fontweight='bold')
    ax.text(0.5, 0.022, "Sources secondaires. Chiffres susceptibles d'évoluer : à revérifier avant chaque session.",
            fontsize=9, ha='center', va='center', color=MUTED, style='italic')
    save(fig, "automne_2026_niveaux_de_preuve.png")


def generate_quotes():
    fig, ax = new_fig("PAROLES DE MATHÉMATICIENS", "Quatre réactions à la publication du 6 octobre 2026 et à ses suites")
    quotes = [
        (0.04, 0.47, GREEN, "ENTHOUSIASME",
         "« Peut-être le jour le plus important\nde l'histoire des mathématiques\nà ce jour. »",
         "Álvaro Lozano-Robledo, mathématicien"),
        (0.515, 0.47, RED, "CHOC",
         "« Le choc est immense.\nJe suis paralysé. »",
         "Hugo Duminil-Copin, médaille Fields 2022"),
        (0.04, 0.095, AMBER, "PRUDENCE",
         "« Les mathématiques sont\nun marathon, pas un sprint. »",
         "Peter Scholze, médaille Fields 2018"),
        (0.515, 0.095, BLUE, "PRINCIPE",
         "« Résoudre des problèmes n'est qu'un outil\nau service du but premier :\nla compréhension. »",
         "Déclaration de 25 médaillés Fields, 11 sept. 2026"),
    ]
    w, h = 0.445, 0.34
    for x, y, col, tag, quote, who in quotes:
        card(ax, x, y, w, h, col)
        ax.text(x + 0.025, y + h - 0.045, tag, fontsize=10, fontweight='bold', ha='left', va='center', color=col)
        ax.text(x + w / 2, y + h * 0.53, quote, fontsize=12.5, style='italic', ha='center', va='center',
                color=INK, linespacing=1.45)
        ax.text(x + w - 0.025, y + 0.04, who, fontsize=9.5, ha='right', va='center', color=MUTED)
    ax.text(0.5, 0.035, "Citations rapportées par The Decoder (12 septembre et 10 octobre 2026). Traductions de l'anglais.",
            fontsize=9, ha='center', va='center', color=MUTED, style='italic')
    save(fig, "automne_2026_reactions.png")


def generate_verification_gap():
    fig, ax = new_fig("« VÉRIFIÉ » NE VEUT PAS DIRE « CONFORME AU BESOIN »",
                      "La vérification porte sur l'énoncé qu'on lui donne, pas sur l'intention")
    cols_x = [0.17, 0.455, 0.74]
    w, h = 0.225, 0.14
    rows = [
        (0.585, "EN MATHÉMATIQUES", ["Problème posé", "Énoncé formel", "Preuve vérifiée"],
         ["Texte de l'article", "Code Lean", "Par la machine"]),
        (0.335, "EN ATELIER", ["Besoin du client", "Spécification", "Contrôle conforme"],
         ["Fonction attendue", "Plan, gamme, cahier des charges", "Rapport d'essai"]),
    ]
    for y, label, names, subs in rows:
        ax.text(0.035, y + h / 2, label.replace(" ", "\n", 1), fontsize=10, fontweight='bold', ha='left', va='center',
                color=MUTED, linespacing=1.4)
        for i, (x, n, s) in enumerate(zip(cols_x, names, subs)):
            card(ax, x, y, w, h, [INK, DEEP, GREEN][i], face=[PANEL, PANEL, '#F0FDF4'][i])
            ax.text(x + w / 2, y + h * 0.63, n, fontsize=11.5, fontweight='bold', ha='center', va='center', color=INK)
            ax.text(x + w / 2, y + h * 0.28, s, fontsize=9, ha='center', va='center', color=MUTED)
        ax.annotate("", xy=(cols_x[1] - 0.012, y + h / 2), xytext=(cols_x[0] + w + 0.012, y + h / 2),
                    arrowprops=dict(arrowstyle="->", color=RED, lw=2.5, linestyle=(0, (3, 2))))
        ax.annotate("", xy=(cols_x[2] - 0.012, y + h / 2), xytext=(cols_x[1] + w + 0.012, y + h / 2),
                    arrowprops=dict(arrowstyle="->", color=GREEN, lw=2.5))

    x_gap = (cols_x[0] + w + cols_x[1]) / 2
    x_ok = (cols_x[1] + w + cols_x[2]) / 2
    ax.text(x_gap, 0.805, "Écart possible", fontsize=11, fontweight='bold', ha='center', va='center', color=RED)
    ax.text(x_gap, 0.767, "Traduction humaine ou IA,\nnon vérifiée automatiquement", fontsize=8.8, ha='center',
            va='center', color=RED, linespacing=1.35)
    ax.text(x_ok, 0.805, "Ce que la machine vérifie", fontsize=11, fontweight='bold', ha='center', va='center', color=GREEN)
    ax.text(x_ok, 0.767, "Chaque étape découle\nde l'énoncé fourni", fontsize=8.8, ha='center', va='center',
            color=GREEN, linespacing=1.35)

    card(ax, 0.17, 0.2, 0.795, 0.085, AMBER, face='#FFFBEB', lw=1.5)
    ax.text(0.5675, 0.2425, "Navier-Stokes : l'article annonce 4 dérivées supplémentaires, le code Lean en utilise 5\n"
            "(Bastounis, Circelli et Hansen, préprint arXiv:2610.08144).", fontsize=9.8, ha='center', va='center',
            color=INK, linespacing=1.45)
    card(ax, 0.035, 0.045, 0.93, 0.095, INK, face=INK, lw=1)
    ax.text(0.5, 0.0925, "Question à poser devant toute sortie d'IA :\n"
            "qu'est-ce qui a été vérifié, par qui, et par rapport à quel énoncé ?", fontsize=11.5, fontweight='bold',
            ha='center', va='center', color='#FFFFFF', linespacing=1.5)
    save(fig, "automne_2026_verifie_ou_conforme.png")


def main():
    generate_timeline()
    generate_status_matrix()
    generate_quotes()
    generate_verification_gap()
    print("4 diagrammes générés dans", OUTPUT_DIR)


if __name__ == "__main__":
    main()

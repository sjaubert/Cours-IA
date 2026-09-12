"""
Régénération de tous les diagrammes et infographies techniques sur FOND BLANC (#FFFFFF)
pour une harmonisation parfaite avec le diaporama original d'Introduction à l'IA.
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Configuration typographique globale Matplotlib
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.family'] = 'sans-serif'


def generate_rag_light():
    fig, ax = plt.subplots(figsize=(12, 7.5), facecolor='#FFFFFF')
    ax.set_facecolor('#FFFFFF')
    ax.axis('off')

    # Titre
    ax.text(0.5, 0.94, "ARCHITECTURE RAG INDUSTRIELLE (Retrieval-Augmented Generation)",
            fontsize=14, fontweight='bold', ha='center', va='center', color='#0F172A')
    ax.text(0.5, 0.88, "Ancrage des réponses dans la documentation d'usine sans réentraînement",
            fontsize=10.5, ha='center', va='center', color='#475569')

    # Cartes d'ingestion (Haut)
    # 1. Documents Usine
    r1 = patches.FancyBboxPatch((0.05, 0.52), 0.26, 0.28, boxstyle="round,pad=0.02,rounding_size=0.03",
                                facecolor='#F8FAFC', edgecolor='#0284C7', linewidth=2)
    ax.add_patch(r1)
    ax.text(0.18, 0.73, "1. Documents Usine", fontsize=11, fontweight='bold', ha='center', color='#0284C7')
    ax.text(0.18, 0.63, "• Manuels machines\n• Gammes d'usinage\n• Schémas électriques\n• Fiches FDS atelier",
            fontsize=9.5, ha='center', va='center', color='#334155')

    # Flèche 1 -> 2
    ax.annotate("", xy=(0.37, 0.66), xytext=(0.32, 0.66),
                arrowprops=dict(arrowstyle="->", color='#0284C7', lw=2.5))

    # 2. Découpage & Embeddings
    r2 = patches.FancyBboxPatch((0.38, 0.52), 0.26, 0.28, boxstyle="round,pad=0.02,rounding_size=0.03",
                                facecolor='#F8FAFC', edgecolor='#2563EB', linewidth=2)
    ax.add_patch(r2)
    ax.text(0.51, 0.73, "2. Embeddings & Chunks", fontsize=11, fontweight='bold', ha='center', color='#2563EB')
    ax.text(0.51, 0.63, "• Découpage sémantique\n• Modèle d'embeddings\n• Vecteurs denses\n• Métadonnées (page, date)",
            fontsize=9.5, ha='center', va='center', color='#334155')

    # Flèche 2 -> 3
    ax.annotate("", xy=(0.70, 0.66), xytext=(0.65, 0.66),
                arrowprops=dict(arrowstyle="->", color='#2563EB', lw=2.5))

    # 3. Base Vectorielle
    r3 = patches.FancyBboxPatch((0.71, 0.52), 0.25, 0.28, boxstyle="round,pad=0.02,rounding_size=0.03",
                                facecolor='#F0FDF4', edgecolor='#16A34A', linewidth=2)
    ax.add_patch(r3)
    ax.text(0.835, 0.73, "3. Base Vectorielle", fontsize=11, fontweight='bold', ha='center', color='#16A34A')
    ax.text(0.835, 0.63, "• Indexation HNSW\n• Chroma / Qdrant\n• Recherche Cosinus\n• Données étanches",
            fontsize=9.5, ha='center', va='center', color='#334155')

    # Cartes d'inférence (Bas)
    # Flèche retour 3 -> 4
    ax.annotate("", xy=(0.51, 0.38), xytext=(0.835, 0.51),
                arrowprops=dict(arrowstyle="->", color='#16A34A', lw=2.5, connectionstyle="arc3,rad=0.2"))

    # 4. Requête Opérateur
    r4 = patches.FancyBboxPatch((0.05, 0.10), 0.26, 0.26, boxstyle="round,pad=0.02,rounding_size=0.03",
                                facecolor='#FEF2F2', edgecolor='#DC2626', linewidth=2)
    ax.add_patch(r4)
    ax.text(0.18, 0.29, "4. Requête Opérateur", fontsize=11, fontweight='bold', ha='center', color='#DC2626')
    ax.text(0.18, 0.20, "« Quel est le couple de\nserrage de la broche\nsur CN Mazak 400 ? »",
            fontsize=9.5, ha='center', va='center', style='italic', color='#334155')

    # Flèche 4 -> 5
    ax.annotate("", xy=(0.37, 0.23), xytext=(0.32, 0.23),
                arrowprops=dict(arrowstyle="->", color='#DC2626', lw=2.5))

    # 5. Recherche Similarité & Contexte
    r5 = patches.FancyBboxPatch((0.38, 0.10), 0.26, 0.26, boxstyle="round,pad=0.02,rounding_size=0.03",
                                facecolor='#FFFBEB', edgecolor='#D97706', linewidth=2)
    ax.add_patch(r5)
    ax.text(0.51, 0.29, "5. Recherche & Contexte", fontsize=11, fontweight='bold', ha='center', color='#D97706')
    ax.text(0.51, 0.20, "• Top-3 extraits pertinents\n• Injection dans le prompt\n• Page 42 - Manuel Mazak\n• Zéro hallucination",
            fontsize=9.5, ha='center', va='center', color='#334155')

    # Flèche 5 -> 6
    ax.annotate("", xy=(0.70, 0.23), xytext=(0.65, 0.23),
                arrowprops=dict(arrowstyle="->", color='#D97706', lw=2.5))

    # 6. Réponse Sourcée
    r6 = patches.FancyBboxPatch((0.71, 0.10), 0.25, 0.26, boxstyle="round,pad=0.02,rounding_size=0.03",
                                facecolor='#EFF6FF', edgecolor='#2563EB', linewidth=2)
    ax.add_patch(r6)
    ax.text(0.835, 0.29, "6. Réponse Sourcée", fontsize=11, fontweight='bold', ha='center', color='#2563EB')
    ax.text(0.835, 0.20, "« 45 N.m avec clé dynamométrique\n(Source : Manuel Mazak p.42) »",
            fontsize=9.5, ha='center', va='center', fontweight='bold', color='#1E3A8A')

    plt.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "rag_architecture.png"), dpi=250, bbox_inches='tight')
    plt.close()


def generate_mcp_light():
    fig, ax = plt.subplots(figsize=(12, 7.5), facecolor='#FFFFFF')
    ax.set_facecolor('#FFFFFF')
    ax.axis('off')

    ax.text(0.5, 0.94, "LE PROTOCOLE OUVERT MCP (Model Context Protocol - Anthropic 2024)",
            fontsize=13.5, fontweight='bold', ha='center', va='center', color='#0F172A')
    ax.text(0.5, 0.88, "Standard ouvert d'interconnexion universelle entre LLM et outils d'entreprise",
            fontsize=10.5, ha='center', va='center', color='#475569')

    # Bloc 1 : Client / Host (Gauche)
    r_host = patches.FancyBboxPatch((0.05, 0.22), 0.26, 0.58, boxstyle="round,pad=0.02,rounding_size=0.03",
                                   facecolor='#EFF6FF', edgecolor='#2563EB', linewidth=2.5)
    ax.add_patch(r_host)
    ax.text(0.18, 0.74, "CLIENT / HÔTE IA", fontsize=12, fontweight='bold', ha='center', color='#1E40AF')
    ax.text(0.18, 0.52, "• Interface Atelier / IDE\n• Modèle LLM (Local/Cloud)\n• Planification d'actions\n• Moteur de raisonnement\n• Contrôle humain (HITL)",
            fontsize=10, ha='center', va='center', color='#1E293B')

    # Bloc 2 : Protocole MCP (Centre)
    r_proto = patches.FancyBboxPatch((0.38, 0.22), 0.24, 0.58, boxstyle="round,pad=0.02,rounding_size=0.03",
                                     facecolor='#F8FAFC', edgecolor='#7C3AED', linewidth=2.5)
    ax.add_patch(r_proto)
    ax.text(0.50, 0.74, "STANDARD MCP", fontsize=12, fontweight='bold', ha='center', color='#6D28D9')
    ax.text(0.50, 0.52, "• JSON-RPC 2.0 sécurisé\n• Découverte d'outils\n• Lecture de ressources\n• Exécution de prompts\n• Isolation des droits",
            fontsize=10, ha='center', va='center', color='#1E293B')

    # Double flèche Host <-> Proto
    ax.annotate("", xy=(0.37, 0.51), xytext=(0.32, 0.51),
                arrowprops=dict(arrowstyle="<->", color='#7C3AED', lw=3))

    # Bloc 3 : Serveurs MCP d'Usine (Droite)
    servers = [
        ("Serveur MCP ERP / SAP", "Stocks pièces & commandes", '#0284C7', 0.62),
        ("Serveur MCP GMAO", "Historique de pannes & MTBF", '#16A34A', 0.42),
        ("Serveur MCP OPC-UA / MQTT", "Télémétrie automates en direct", '#EA580C', 0.22)
    ]
    for s_title, s_desc, col, y_pos in servers:
        box = patches.FancyBboxPatch((0.69, y_pos), 0.27, 0.17, boxstyle="round,pad=0.02,rounding_size=0.03",
                                     facecolor='#FFFFFF', edgecolor=col, linewidth=2)
        ax.add_patch(box)
        ax.text(0.825, y_pos + 0.11, s_title, fontsize=10.5, fontweight='bold', ha='center', color=col)
        ax.text(0.825, y_pos + 0.05, s_desc, fontsize=9, ha='center', color='#475569')
        # Flèche Proto -> Server
        ax.annotate("", xy=(0.68, y_pos + 0.085), xytext=(0.63, y_pos + 0.085),
                    arrowprops=dict(arrowstyle="<->", color=col, lw=2))

    plt.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "mcp_protocol_architecture.png"), dpi=250, bbox_inches='tight')
    plt.close()


def generate_reasoning_light():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 7.2), facecolor='#FFFFFF')
    ax1.set_facecolor('#F8FAFC')
    ax2.set_facecolor('#F8FAFC')

    for ax in [ax1, ax2]:
        for spine in ax.spines.values():
            spine.set_color('#CBD5E1')
            spine.set_linewidth(1.5)

    # Axe 1 : Système 1
    ax1.set_title("SYSTEME 1 : GENERATION REFLEXE\n(LLM Classique - GPT-4, Llama standard)",
                  fontsize=11.5, fontweight='bold', color='#DC2626', pad=15)
    steps_s1 = [
        ("Prompt Utilisateur", '#FEF2F2', '#DC2626'),
        ("Prédiction Statistique Directe\n(Token par Token)", '#FFFFFF', '#94A3B8'),
        ("Réponse Immédiate Sans Recul\nRisque élevé d'erreur logique", '#FEE2E2', '#B91C1C')
    ]
    y = 0.8
    for title, bg, border in steps_s1:
        rect = patches.FancyBboxPatch((0.1, y - 0.15), 0.8, 0.15, boxstyle="round,pad=0.02,rounding_size=0.03",
                                     facecolor=bg, edgecolor=border, linewidth=2)
        ax1.add_patch(rect)
        ax1.text(0.5, y - 0.075, title, ha='center', va='center', fontsize=10, fontweight='bold', color='#0F172A')
        if y > 0.35:
            ax1.annotate("", xy=(0.5, y - 0.20), xytext=(0.5, y - 0.16),
                         arrowprops=dict(arrowstyle="->", color='#DC2626', lw=2.5))
        y -= 0.28
    ax1.axis('off')

    # Axe 2 : Système 2
    ax2.set_title("SYSTEME 2 : DELIBERATION LOGIQUE\n(Modèles de Raisonnement - o1, DeepSeek-R1)",
                  fontsize=11.5, fontweight='bold', color='#059669', pad=15)
    steps_s2 = [
        ("Prompt Complexe (Multi-contraintes)", '#F0FDF4', '#059669'),
        ("Tokens de Réflexion Cachés (Chain-of-Thought)\nDécomposition étape par étape", '#EFF6FF', '#2563EB'),
        ("Vérification & Backtracking\nAuto-correction des déductions erronées", '#FEF3C7', '#D97706'),
        ("Conclusion Rigoureusement Validée\nZéro hallucination mathématique", '#ECFDF5', '#047857')
    ]
    y = 0.85
    for title, bg, border in steps_s2:
        rect = patches.FancyBboxPatch((0.08, y - 0.13), 0.84, 0.13, boxstyle="round,pad=0.02,rounding_size=0.03",
                                     facecolor=bg, edgecolor=border, linewidth=2)
        ax2.add_patch(rect)
        ax2.text(0.5, y - 0.065, title, ha='center', va='center', fontsize=9.5, fontweight='bold', color='#0F172A')
        if y > 0.3:
            ax2.annotate("", xy=(0.5, y - 0.17), xytext=(0.5, y - 0.14),
                         arrowprops=dict(arrowstyle="->", color='#059669', lw=2.2))
        y -= 0.22
    ax2.axis('off')

    plt.suptitle("PARADIGME COGNITIF : SYSTEME 1 vs SYSTEME 2 EN INDUSTRIE",
                 fontsize=13.5, fontweight='bold', color='#0F172A', y=0.98)
    plt.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "reasoning_chain_of_thought.png"), dpi=250, bbox_inches='tight')
    plt.close()


def generate_multimodal_light():
    fig, ax = plt.subplots(figsize=(12, 7.5), facecolor='#FFFFFF')
    ax.set_facecolor('#FFFFFF')
    ax.axis('off')

    ax.text(0.5, 0.94, "L'IA MULTIMODALE EN ATELIER DE PRODUCTION",
            fontsize=14, fontweight='bold', ha='center', va='center', color='#0F172A')
    ax.text(0.5, 0.88, "Fusion des signaux physiques hétérogènes dans un même espace sémantique",
            fontsize=10.5, ha='center', va='center', color='#475569')

    # Entrées hétérogènes (Gauche)
    inputs = [
        ("Vision Haute Cadence", "Images de pièces & caméras d'usinage", '#0284C7', 0.68),
        ("Signaux Capteurs", "Télémétrie vibratoire & thermique", '#16A34A', 0.44),
        ("Documentation & Logs", "Historique GMAO & fiches qualité", '#EA580C', 0.20)
    ]
    for title, desc, col, y_pos in inputs:
        b = patches.FancyBboxPatch((0.05, y_pos), 0.27, 0.18, boxstyle="round,pad=0.02,rounding_size=0.03",
                                   facecolor='#F8FAFC', edgecolor=col, linewidth=2)
        ax.add_patch(b)
        ax.text(0.185, y_pos + 0.11, title, fontsize=11, fontweight='bold', ha='center', color=col)
        ax.text(0.185, y_pos + 0.05, desc, fontsize=8.5, ha='center', color='#475569')
        # Flèche vers le centre
        ax.annotate("", xy=(0.42, 0.51), xytext=(0.33, y_pos + 0.09),
                    arrowprops=dict(arrowstyle="->", color=col, lw=2.5))

    # Cœur multimodal (Centre)
    core = patches.FancyBboxPatch((0.43, 0.25), 0.22, 0.52, boxstyle="round,pad=0.02,rounding_size=0.03",
                                  facecolor='#EFF6FF', edgecolor='#2563EB', linewidth=2.5)
    ax.add_patch(core)
    ax.text(0.54, 0.69, "ESPACE LATENT\nPARTAGÉ", fontsize=11.5, fontweight='bold', ha='center', color='#1E40AF')
    ax.text(0.54, 0.46, "Alignement sémantique\nmultimodal :\n\n• Projection conjointe\n• Corrélation temps réel\n• Attention croisée",
            fontsize=9.5, ha='center', va='center', color='#1E293B')

    # Sorties industrielles (Droite)
    outputs = [
        ("Contrôle Qualité 100%", "Détection millimétrique de défauts", '#059669', 0.68),
        ("Maintenance Prédictive", "Diagnostic précoce de roulements", '#7C3AED', 0.44),
        ("Aide Opérateur Terrain", "Consignes pas-à-pas sur tablette", '#2563EB', 0.20)
    ]
    for title, desc, col, y_pos in outputs:
        b = patches.FancyBboxPatch((0.71, y_pos), 0.25, 0.18, boxstyle="round,pad=0.02,rounding_size=0.03",
                                   facecolor='#F8FAFC', edgecolor=col, linewidth=2)
        ax.add_patch(b)
        ax.text(0.835, y_pos + 0.11, title, fontsize=11, fontweight='bold', ha='center', color=col)
        ax.text(0.835, y_pos + 0.05, desc, fontsize=8.5, ha='center', color='#475569')
        # Flèche du centre vers la sortie
        ax.annotate("", xy=(0.70, y_pos + 0.09), xytext=(0.66, 0.51),
                    arrowprops=dict(arrowstyle="->", color=col, lw=2.5))

    plt.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "multimodal_industrial_ai.png"), dpi=250, bbox_inches='tight')
    plt.close()


def generate_sovereignty_light():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 7.2), facecolor='#FFFFFF')
    ax1.set_facecolor('#FFFBEB')
    ax2.set_facecolor('#F0FDF4')

    for ax, col in [(ax1, '#F59E0B'), (ax2, '#10B981')]:
        for spine in ax.spines.values():
            spine.set_color(col)
            spine.set_linewidth(2)

    ax1.set_title("CLOUD PROPRIÉTAIRE (AMÉRICAIN)\nRisques de dépendance & conformité",
                  fontsize=11.5, fontweight='bold', color='#B45309', pad=15)
    pts1 = [
        "• Extraterritorialité juridique (Cloud Act US)",
        "• Risque de fuite de propriété intellectuelle",
        "• Dépendance aux tarifs et quotas d'API",
        "• Latence réseau incompatible temps réel usine",
        "• Modèles boîtes noires non auditables"
    ]
    y = 0.8
    for p in pts1:
        ax1.text(0.08, y, p, fontsize=10.5, color='#78350F')
        y -= 0.14
    ax1.axis('off')

    ax2.set_title("MODÈLES OUVERTS & SOUVERAINS (OPEN-WEIGHTS)\nMaîtrise totale On-Premise (Usine)",
                  fontsize=11.5, fontweight='bold', color='#047857', pad=15)
    pts2 = [
        "• Hébergement local en réseau étanche (Air-Gapped)",
        "• Modèles européens d'excellence (Mistral AI)",
        "• Modèles ouverts mondiaux (Llama, Qwen)",
        "• Coût par requête nul en régime d'atelier",
        "• Personnalisation sans limite sur lexiques métier"
    ]
    y = 0.8
    for p in pts2:
        ax2.text(0.08, y, p, fontsize=10.5, color='#064E3B')
        y -= 0.14
    ax2.axis('off')

    plt.suptitle("SOUVERAINETÉ NUMÉRIQUE & MODÈLES OUVERTS EN INDUSTRIE",
                 fontsize=14, fontweight='bold', color='#0F172A', y=0.98)
    plt.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "sovereign_open_weights_models.png"), dpi=250, bbox_inches='tight')
    plt.close()


def generate_frugal_light():
    fig, ax = plt.subplots(figsize=(11, 6.8), facecolor='#FFFFFF')
    ax.set_facecolor('#F8FAFC')

    categories = ['Modèle Compact\n1.5B (4-bit)', 'Modèle Atelier\n7B - 8B (4-bit)', 'Modèle Avancé\n14B - 32B (4-bit)', 'Modèle Géant Cloud\n70B - 405B (FP16)']
    vram_gb = [1.2, 5.2, 18.0, 150.0]
    colors = ['#10B981', '#0284C7', '#F59E0B', '#EF4444']

    bars = ax.bar(categories, vram_gb, color=colors, width=0.55, edgecolor='#334155', linewidth=1.5)
    ax.set_yscale('log')
    ax.set_ylabel("Empreinte Mémoire VRAM requise (Go - Échelle Log)", fontsize=11, color='#0F172A')
    ax.set_title("EFFICIENCE NUMÉRIQUE & FRUGALITÉ : EMPREINTE VRAM SELON LA TAILLE DU MODÈLE\nComparatif après quantification INT4 (AWQ / GGUF)",
                 fontsize=12, fontweight='bold', color='#0F172A', pad=15)
    ax.grid(axis='y', linestyle='--', alpha=0.4, color='#94A3B8')
    ax.tick_params(colors='#334155', labelsize=10)

    for bar, val in zip(bars, vram_gb):
        ax.text(bar.get_x() + bar.get_width()/2, val * 1.15, f"{val} Go",
                ha='center', va='bottom', fontsize=11, fontweight='bold', color='#0F172A')

    # Annotations
    ax.text(0.28, 0.25, "Embarquable sur\nPC industriel ou NPU", transform=ax.transAxes,
            ha='center', fontsize=9.5, color='#047857', fontweight='bold',
            bbox=dict(boxstyle="round,pad=0.3", fc="#ECFDF5", ec="#10B981"))

    ax.text(0.85, 0.70, "Nécessite datacenter\nmulti-GPU dédié", transform=ax.transAxes,
            ha='center', fontsize=9.5, color='#991B1B', fontweight='bold',
            bbox=dict(boxstyle="round,pad=0.3", fc="#FEF2F2", ec="#EF4444"))

    plt.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "frugal_ai_comparison.png"), dpi=250, bbox_inches='tight')
    plt.close()


def generate_energy_light():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6.8), facecolor='#FFFFFF')
    ax1.set_facecolor('#F8FAFC')
    ax2.set_facecolor('#F8FAFC')

    # Bar chart
    categories = ['Recherche Web\nClassique', 'Requête LLM 7B\nLocal (4-bit)', 'Requête LLM 70B\nDatacenter', 'Modèle Raisonnement\n(o1 / R1)']
    conso_wh = [0.3, 1.2, 4.5, 18.0]
    colors = ['#10B981', '#0284C7', '#F59E0B', '#EF4444']

    bars = ax1.bar(categories, conso_wh, color=colors, width=0.55, edgecolor='#334155', linewidth=1.2)
    ax1.set_title("Consommation Électrique par Requête (Wh)\nSource : Luccioni et al. (2023) / AIE (2024)",
                  fontsize=11, fontweight='bold', color='#0F172A', pad=12)
    ax1.set_ylabel("Énergie par requête (Watt-heure)", fontsize=10, color='#0F172A')
    ax1.tick_params(colors='#334155', labelsize=9.5)
    ax1.grid(axis='y', linestyle='--', alpha=0.4, color='#94A3B8')

    for bar, val in zip(bars, conso_wh):
        ax1.text(bar.get_x() + bar.get_width()/2, val + 0.4, f"{val} Wh",
                 ha='center', va='bottom', fontsize=10.5, fontweight='bold', color='#0F172A')

    # Pie chart
    labels = ['Inférence en Production (75%)', 'Fine-Tuning Spécifique (15%)', 'Entraînement Initial (10%)']
    sizes = [75, 15, 10]
    pie_colors = ['#0284C7', '#818CF8', '#F43F5E']

    wedges, texts, autotexts = ax2.pie(sizes, explode=(0.05, 0, 0), labels=labels, autopct='%1.0f%%',
                                       startangle=140, colors=pie_colors,
                                       textprops=dict(color='#0F172A', fontsize=10, fontweight='bold'),
                                       wedgeprops=dict(edgecolor='#FFFFFF', linewidth=2))
    for autotext in autotexts:
        autotext.set_color('#FFFFFF')
        autotext.set_fontsize(11)

    ax2.set_title("Cycle de Vie Énergétique d'un Modèle Industriel\n(90% de l'empreinte en phase d'usage)",
                  fontsize=11, fontweight='bold', color='#0F172A', pad=12)

    plt.suptitle("BILAN ÉNERGÉTIQUE & EMPREINTE CARBONE DE L'IA INDUSTRIELLE",
                 fontsize=13.5, fontweight='bold', color='#0F172A', y=0.98)
    plt.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "energy_footprint_ai.png"), dpi=250, bbox_inches='tight')
    plt.close()


def generate_biases_light():
    fig, ax = plt.subplots(figsize=(13, 7.2), facecolor='#FFFFFF')
    ax.set_facecolor('#FFFFFF')
    ax.axis('off')

    ax.text(0.5, 0.94, "LES 4 PIÈGES COGNITIFS DE L'INGÉNIEUR FACE À L'IA",
            fontsize=14, fontweight='bold', ha='center', va='center', color='#0F172A')
    ax.text(0.5, 0.88, "Matrice des biais décisionnels et contre-mesures de supervision critique",
            fontsize=10.5, ha='center', va='center', color='#475569')

    quadrants = [
        (0.05, 0.48, 0.42, 0.35, "1. BIAIS D'AUTOMATISATION",
         "Délégation aveugle de la décision",
         "• Confiance excessive dans le résultat du modèle\n• Négligence du contrôle physique contradictoire\n• Risque critique sur sécurités machines",
         "Garde-fous : Procédure de double vérification humaine obligatoire",
         '#DC2626', '#FEF2F2'),

        (0.53, 0.48, 0.42, 0.35, "2. ILLUSION DE COMPÉTENCE",
         "Éloquence confondue avec exactitude",
         "• Le LLM s'exprime avec une autorité trompeuse\n• Masquage des failles physiques sous un style fluide\n• Hallucinations subtiles sur normes ISO",
         "Garde-fous : Ancrage RAG strict sur manuels vérifiés",
         '#D97706', '#FFFBEB'),

        (0.05, 0.08, 0.42, 0.35, "3. BIAIS DE CONFIRMATION",
         "Instrumentalisation de l'IA",
         "• Utiliser l'IA pour valider son intuition initiale\n• Omission de tester les cas limites de rupture\n• Prompt orienté confirmant l'erreur de calcul",
         "Garde-fous : Prompting d'avocat du diable (challenge critique)",
         '#2563EB', '#EFF6FF'),

        (0.53, 0.08, 0.42, 0.35, "4. ATROPHIE DES COMPÉTENCES",
         "Perte d'expertise fondamentale",
         "• Incapacité progressive à diagnostiquer sans outil\n• Dégradation des connaissances métier de base\n• Dépendance algorithmique irréversible",
         "Garde-fous : Maintien d'ateliers manuels 'sans IA' réguliers",
         '#7C3AED', '#FAF5FF')
    ]

    for x, y, w, h, title, sub, desc, gf, col, bg in quadrants:
        b = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.03",
                                   facecolor=bg, edgecolor=col, linewidth=2)
        ax.add_patch(b)
        ax.text(x + w/2, y + h - 0.05, title, fontsize=11, fontweight='bold', ha='center', color=col)
        ax.text(x + w/2, y + h - 0.10, sub, fontsize=9.5, style='italic', ha='center', color='#475569')
        ax.text(x + 0.02, y + 0.12, desc, fontsize=8.8, va='center', color='#1E293B')

        # Bandeau bas garde-fous
        gfb = patches.Rectangle((x + 0.015, y + 0.02), w - 0.03, 0.065, facecolor='#FFFFFF', edgecolor=col, linewidth=1)
        ax.add_patch(gfb)
        ax.text(x + w/2, y + 0.052, gf, fontsize=8.5, fontweight='bold', ha='center', va='center', color=col)

    plt.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "metacognition_biases_matrix.png"), dpi=250, bbox_inches='tight')
    plt.close()


def generate_roadmap_light():
    fig, ax = plt.subplots(figsize=(14, 7.2), facecolor='#FFFFFF')
    ax.set_facecolor('#FFFFFF')
    ax.axis('off')

    steps = [
        ("ÉTAPE 1 : CADRAGE & ROI", '#0284C7', '#F0F9FF', [
            "• Qualification du cas d'usage",
            "• Évaluation du ROI industriel",
            "• Matrice de criticité AI Act",
            "• Audit qualité données atelier"
        ]),
        ("ÉTAPE 2 : SOUVERAINETÉ", '#2563EB', '#EFF6FF', [
            "• Choix du modèle : SLM vs LLM",
            "• Déploiement On-Premise / Edge",
            "• Quantification 4-bit / 8-bit",
            "• Isolation réseau usine étanche"
        ]),
        ("ÉTAPE 3 : RAG & MCP", '#7C3AED', '#FAF5FF', [
            "• Indexation manuels machines",
            "• Connecteurs MCP (ERP/GMAO)",
            "• Passerelles automates OPC-UA",
            "• Garde-fous anti-hallucinations"
        ]),
        ("ÉTAPE 4 : GOUVERNANCE", '#059669', '#ECFDF5', [
            "• Dossier technique AI Act",
            "• Surveillance dérive (Drift)",
            "• Formation des équipes atelier",
            "• Boucle de contrôle humain"
        ])
    ]

    for idx, (title, col, bg, bullets) in enumerate(steps):
        x = 0.03 + idx * 0.245
        y = 0.12
        w = 0.225
        h = 0.72

        rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.03",
                                     facecolor=bg, edgecolor=col, linewidth=2.5)
        ax.add_patch(rect)

        # Header box
        hdr = patches.Rectangle((x, y + h - 0.13), w, 0.13, facecolor=col, edgecolor=col)
        ax.add_patch(hdr)
        ax.text(x + w/2, y + h - 0.065, title, color='#FFFFFF', fontsize=10.5, fontweight='bold', ha='center', va='center')

        # Bullets
        by = y + h - 0.20
        for b in bullets:
            ax.text(x + 0.015, by, b, color='#0F172A', fontsize=10, ha='left', va='top')
            by -= 0.11

        # Flèche entre étapes
        if idx < 3:
            ax.annotate('', xy=(x + w + 0.018, y + h/2), xytext=(x + w + 0.002, y + h/2),
                        arrowprops=dict(arrowstyle='->', color='#0284C7', lw=3))

    ax.text(0.5, 0.94, 'FEUILLE DE ROUTE MÉTHODOLOGIQUE DE L\'INGÉNIEUR 2026',
            color='#0F172A', fontsize=15, fontweight='bold', ha='center', va='center')
    ax.text(0.5, 0.88, 'Cycle d\'industrialisation conforme aux normes AFNOR Spec IA et AI Act européen',
            color='#475569', fontsize=10.5, ha='center', va='center')

    plt.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "industrial_ai_roadmap_2026.png"), dpi=250, bbox_inches='tight')
    plt.close()


def generate_ai_act_pyramid_light():
    fig, ax = plt.subplots(figsize=(11, 7.2), facecolor='#FFFFFF')
    ax.set_facecolor('#FFFFFF')
    ax.axis('off')

    ax.text(0.5, 0.95, "LÉGISLATION EUROPÉENNE SUR L'IA (AI ACT — RÈGLEMENT UE 2024/1689)",
            fontsize=13, fontweight='bold', ha='center', va='center', color='#0F172A')
    ax.text(0.5, 0.89, "Classification des Systèmes d'IA par Niveaux de Risque",
            fontsize=10.5, ha='center', va='center', color='#475569')

    # Niveaux de la pyramide (du haut vers le bas)
    levels = [
        # (y_top, y_bottom, w_top, w_bottom, col_fill, col_edge, title, subtitle, ex)
        (0.82, 0.65, 0.28, 0.44, '#FEF2F2', '#DC2626', "1. RISQUE INACCEPTABLE (INTERDIT)", "Manipulation cognitive, notation sociale, biométrie temps réel non autorisée"),
        (0.64, 0.46, 0.46, 0.62, '#FFFBEB', '#D97706', "2. HAUT RISQUE (FORTEMENT ENCADRÉ)", "Sécurité machines, cobotique, tri RH, infrastructures critiques"),
        (0.45, 0.28, 0.64, 0.80, '#EFF6FF', '#2563EB', "3. RISQUE SPÉCIFIQUE (TRANSPARENCE)", "Chatbots, deepfakes, génération de contenu : étiquetage obligatoire"),
        (0.27, 0.10, 0.82, 0.96, '#F0FDF4', '#16A34A', "4. RISQUE MINIMAL OU NUL (USAGE LIBRE)", "Filtres anti-spam, IA de jeux vidéo, optimisation d'usinage interne")
    ]

    for y_top, y_bottom, w_top, w_bottom, fc, ec, title, desc in levels:
        h = y_top - y_bottom
        pts = [
            (0.5 - w_top/2, y_top),
            (0.5 + w_top/2, y_top),
            (0.5 + w_bottom/2, y_bottom),
            (0.5 - w_bottom/2, y_bottom)
        ]
        poly = patches.Polygon(pts, facecolor=fc, edgecolor=ec, linewidth=2)
        ax.add_patch(poly)

        y_center = (y_top + y_bottom) / 2
        ax.text(0.5, y_center + 0.025, title, fontsize=10.5, fontweight='bold', ha='center', va='center', color=ec)
        ax.text(0.5, y_center - 0.03, desc, fontsize=8.8, ha='center', va='center', color='#1E293B')

    plt.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "ai_act_risk_pyramid.png"), dpi=250, bbox_inches='tight')
    plt.close()


def main():
    print("Génération de tous les diagrammes en version LIGHT (Fond Blanc)...")
    generate_rag_light()
    print("  -> RAG généré")
    generate_mcp_light()
    print("  -> MCP généré")
    generate_reasoning_light()
    print("  -> Reasoning généré")
    generate_multimodal_light()
    print("  -> Multimodal généré")
    generate_sovereignty_light()
    print("  -> Souveraineté généré")
    generate_frugal_light()
    print("  -> Frugalité généré")
    generate_energy_light()
    print("  -> Énergie généré")
    generate_biases_light()
    print("  -> Biais généré")
    generate_roadmap_light()
    print("  -> Roadmap générée")
    generate_ai_act_pyramid_light()
    print("  -> AI Act Pyramide générée")
    print("Tous les diagrammes LIGHT ont été générés avec succès !")


if __name__ == "__main__":
    main()

# 🌀 Orbite — Jeu de réflexes orbital

Survivez le plus longtemps possible en orbite autour d'un soleil, en évitant les astéroïdes.

**[🎮 Jouer en ligne](https://docdavkitty.github.io/orbite-game/)**

---

## 🎯 Gameplay

- **3 orbites concentriques** — changez de trajectoire (↑↓) pour esquiver
- **Dash latéral** (Espace) — permet une esquive rapide (cooldown ~2s)
- **Orbites dynamiques** — les rayons des orbites oscillent, forçant l'adaptation
- Difficulté progressive : vitesse, densité et types d'ennemis évoluent avec le niveau

## 🚀 Power-ups

| Icône | Nom | Effet |
|-------|-----|-------|
| 🛡️ | **Bouclier** | Absorbe 1 collision, dure ~10s |
| ⏱️ | **Slow-mo** | Ralentit les astéroïdes 50% pendant ~5s |
| ⚡ | **Multi-dash** | Dashes illimités sans cooldown pendant ~6s |
| 🧲 | **Aimant** | Attire les gems dans un rayon 3× plus grand |

## 💎 Gems

Des diamants flottent sur les orbites. Collectez-les pour un bonus de score (50 + 10×niveau).

## 👾 Types d'ennemis

- **Normal** — approche rectiligne classique
- **Exploseur** 💥 — se fragmente en petits éclats à l'impact ou près du soleil
- **Traqueur** 🎯 — ajuste sa trajectoire vers votre position
- **Tournoyeur** 🔄 — orbite autour du soleil, change parfois de sens
- **Fragment** — petit débris issu d'un exploseur, disparaît après un moment

## 🎨 5 Palettes de couleurs

**Tab** ou bouton pour changer : Néon, Magma, Glacier, Toxique, Noir

## 🔊 Effets sonores

Tous les sons sont générés procéduralement (Web Audio API) — aucun fichier nécessaire.

- Collecte de gem / power-up ✨
- Dash 🎵
- Explosion / collision 💥
- Changement de niveau 🎉

## 🏆 Classement en ligne

Le leaderboard tourne sur **`localhost:8081`** (serveur Python stdlib, zéro dépendance).

```
python3 server.py &
```

Puis ouvrez `index.html` ou [le site GitHub Pages](https://docdavkitty.github.io/orbite-game/).

Votre score est sauvegardé localement **et** peut être envoyé au leaderboard après une partie.

## 🛠️ Stack technique

- **100% vanilla** — HTML/CSS/JS, zéro framework, zéro dépendance
- **Backend leaderboard** — Python stdlib (http.server + SQLite)
- **Son** — Web Audio API (synthèse procédurale)
- **Canvas** rendu 2D avec particules, ombres, dégradés

## 🚀 Déploiement

### GitHub Pages (jouable partout)
Déjà en ligne sur `gh-pages` : **[https://docdavkitty.github.io/orbite-game/](https://docdavkitty.github.io/orbite-game/)**
Le leaderboard nécessite le serveur local.

### Local
```bash
# Serveur leaderboard (optionnel)
python3 server.py &

# Ouvre index.html dans le navigateur
```

---

Fait avec 🧠 par [Hermes Agent](https://hermes-agent.nousresearch.com)

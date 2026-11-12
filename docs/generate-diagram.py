"""Regenerate the editable Excalidraw scene and matching SVG using only stdlib."""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASE = "545e1ed4580e147c742bd4d831550bb3ca3da674"
elements = []
svg = []


def element(kind, x, y, width, height, **extra):
    result = dict(id=f"e{len(elements) + 1}", type=kind, x=x, y=y,
                  width=width, height=height, angle=0, strokeColor="#172b4d",
                  backgroundColor="transparent", fillStyle="solid", strokeWidth=1,
                  strokeStyle="solid", roughness=0, opacity=100, groupIds=[],
                  frameId=None, roundness=None, seed=len(elements) + 1, version=1,
                  versionNonce=len(elements) + 1, isDeleted=False, boundElements=None,
                  updated=1, link=None, locked=False)
    result.update(extra)
    elements.append(result)
    return result


def text(x, y, content, size=18, color="#172b4d"):
    lines = content.splitlines()
    width = max(len(line) for line in lines) * size * 0.61
    height = len(lines) * size * 1.3
    element("text", x, y, width, height, text=content, originalText=content,
            fontSize=size, fontFamily=2, textAlign="left", verticalAlign="top",
            containerId=None, autoResize=True, lineHeight=1.3, strokeColor=color)
    for i, line in enumerate(lines):
        svg.append(f'<text x="{x}" y="{y + size + i * size * 1.3}" font-size="{size}" fill="{color}">{html.escape(line)}</text>')


def box(x, y, width, title, content, color):
    height = 148
    element("rectangle", x, y, width, height, backgroundColor=color)
    svg.append(f'<rect x="{x}" y="{y}" width="{width}" height="{height}" fill="{color}" stroke="#172b4d"/>')
    text(x + 18, y + 14, title, 21)
    text(x + 18, y + 49, content, 17)


def arrow(x, y, length):
    element("arrow", x, y, 0, length, points=[[0, 0], [0, length]],
            lastCommittedPoint=None, startBinding=None, endBinding=None,
            startArrowhead=None, endArrowhead="arrow", elbowed=False)
    svg.append(f'<path d="M{x} {y}v{length}m-6 -8 6 8 6 -8" fill="none" stroke="#172b4d" stroke-width="2"/>')


text(30, 22, "Ralph: execution boundaries", 30)
text(30, 67, "Source-backed explanation • not a sandbox or completion guarantee", 18)
text(30, 110, "SHELL IMPLEMENTATION", 17, "#245846")
text(570, 110, "PROMPT-REQUESTED BEHAVIOR", 17, "#765418")
box(30, 148, 500, "1  Prepare script-local state", "prd.json / progress.txt / .last-branch\nBranch-name change: copy current state\nto dated archive; reset progress.", "#e8f3ed")
box(570, 148, 500, "A  Select and implement", "Read PRD + progress; select branch.\nChoose one highest-priority story.\nImplement it and update learnings.", "#fff3d9")
arrow(280, 302, 28)
arrow(820, 302, 28)
box(30, 338, 500, "2  Invoke fresh Amp each iteration", "Prompt piped over stdin. CWD unchanged.\n--dangerously-allow-all; billable usage.\nInvocation errors tolerated (|| true).", "#e8f3ed")
box(570, 338, 500, "B  Check and record", "Run project checks + UI verification.\nCommit only if checks pass; set passes.\nAppend progress and request completion.", "#fff3d9")
arrow(280, 492, 28)
arrow(820, 492, 28)
box(30, 528, 500, "3  Inspect output marker", "COMPLETE marker => exit 0. Otherwise\nrepeat (default limit 10); then exit 1.\nNo independent story/test verification.", "#e8f3ed")
box(570, 528, 500, "Boundary: instructions are not gates", "Shell does not enforce branch policy,\npassing tests, review or truthful status.\nReact presentation runs none of this.", "#fff3d9")
text(30, 710, "Before intentional execution", 23)
text(30, 750, "Resolve copied prompt paths vs. script-local state; review permissions, billing and recovery.\nKeep secrets/private context out of shared logs, archives and agent thread links.", 18)
text(30, 827, "Credits: Ryan Carson implementation; Geoffrey Huntley pattern; JD-attributed CI/ref delta.\nSchematic: Reason-assisted documentation. Inherited code/artwork rights unresolved.", 16)
text(30, 886, f"Source baseline: {BASE} • ralph.sh + prompt.md", 14)
scene = dict(type="excalidraw", version=2, source="https://excalidraw.com",
             elements=elements, appState=dict(viewBackgroundColor="#ffffff", gridSize=None), files={})
(ROOT / "ralph-boundaries.excalidraw").write_text(json.dumps(scene, indent=2) + "\n")
(ROOT / "ralph-boundaries.svg").write_text(
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 930" role="img" aria-labelledby="title desc">'
    '<title id="title">Ralph execution boundaries</title>'
    '<desc id="desc">Shell-enforced state and loop operations contrasted with prompt-requested quality checks and commits. Credits and license limits included.</desc>'
    '<rect width="1100" height="930" fill="white"/>'
    '<g font-family="Arial, sans-serif">' + ''.join(svg) + '</g></svg>\n')
print(f"Generated {len(elements)} editable elements and SVG preview.")

import base64

# Read the face image
with open('face.jpg', 'rb') as f:
    face_b64 = base64.b64encode(f.read()).decode('utf-8')

# Read the HTML file
with open('index.html', 'r') as f:
    html = f.read()

# Replace the image URL with base64
old_url = "https://kela-stag.blr1.digitaloceanspaces.com/mogra/mogra/llm/images/1767867657578-0654106c.jpg"
new_url = f"data:image/jpeg;base64,{face_b64}"
html = html.replace(old_url, new_url)

# Write the updated HTML
with open('index.html', 'w') as f:
    f.write(html)

print(f"Done! Embedded {len(face_b64)} chars of base64")

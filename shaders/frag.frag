#version 130

// Uniform color (RGBA)
uniform vec4 color;

out vec4 fragColor;

void main() {
    fragColor = color;  // Set the output color
}

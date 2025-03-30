#version 130

// Uniform color (RGBA)
uniform vec4 modelColor; //MUST BE SET TO modelColor

out vec4 fragColor;

void main() {
    fragColor = modelColor;  // Set the output color
}

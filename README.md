# Grayscaling Images with Python
Image dimensionality reduction with python through grayscaling

In this repository was used 5 types of grayscaling techniques:
1. Luminiscence (Luma)
    - $\text{Gray} = 0.299R + 0.587G + 0.114B$
2. Averaging
    - $\text{Gray} = \frac{R + G + B}{3}$
3. Desaturation
    - $\text{Gray} = \frac{\text{Max}(R, G, B) + \text{Min}(R, G, B)}{2}$
4. Decomposition
    - Maximum: $\text{Gray} = \text{Max}(R, G, B)$
    - Minimum: $\text{Gray} = \text{Min}(R, G, B)$
5. Single color channel: which uses only one of RGB color channels
    - Red: $\text{Gray} = R$
    - Green: $\text{Gray} = G$
    - Blue: $\text{Gray} = B$

## References
- HELLAND, Tanner. **Seven grayscale conversion algorithms (with pseudocode and VB6 source code)**. Oct 11<sup>th</sup>, 2021. Available at: https://tannerhelland.com/2011/10/01/grayscale-image-algorithm-vb6.html. Accessed on May 20<sup>th</sup>, 2025.
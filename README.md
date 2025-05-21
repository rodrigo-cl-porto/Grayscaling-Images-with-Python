# Grayscaling Images with Python
Image dimensionality reduction with python through grayscaling.

## Grayscaling methods
In this repository was used 5 types of grayscaling techniques:
1. Luminiscence (*Luma*)
    - $\textcolor{gray}{\text{Gray}} = 0.299\textcolor{red}{R} + 0.587\textcolor{green}{G} + 0.114\textcolor{blue}{B}$
2. Averaging
    - $\textcolor{gray}{\text{Gray}} = \frac{\textcolor{red}{R} + \textcolor{green}{G} + \textcolor{blue}{B}}{3}$
3. Desaturation
    - $\textcolor{gray}{\text{Gray}} = \frac{\text{Max}(\textcolor{red}{R}, \textcolor{green}{G}, \textcolor{blue}{B}) + \text{Min}(\textcolor{red}{R}, \textcolor{green}{G}, \textcolor{blue}{B})}{2}$
4. Decomposition
    - Maximum: $\textcolor{gray}{\text{Gray}} = \text{Max}(\textcolor{red}{R}, \textcolor{green}{G}, \textcolor{blue}{B})$
    - Minimum: $\textcolor{gray}{\text{Gray}} = \text{Min}(\textcolor{red}{R}, \textcolor{green}{G}, \textcolor{blue}{B})$
5. Single color channel: which uses only one of RGB color channels
    - Red: $\textcolor{gray}{\text{Gray}} = \textcolor{red}{R}$
    - Green: $\textcolor{gray}{\text{Gray}} = \textcolor{green}{G}$
    - Blue: $\textcolor{gray}{\text{Gray}} = \textcolor{blue}{B}$

## References
- HELLAND, Tanner. **Seven grayscale conversion algorithms (with pseudocode and VB6 source code)**. Oct 11<sup>th</sup>, 2021. Available at: https://tannerhelland.com/2011/10/01/grayscale-image-algorithm-vb6.html. Accessed on May 20<sup>th</sup>, 2025.

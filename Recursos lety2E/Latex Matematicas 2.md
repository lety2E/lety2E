# 1 operaciones con fracciones

\\documentclass\[11pt\]{article}  
\\usepackage\[margin=1.5cm\]{geometry}  
\\usepackage{fontspec}  
\\setmainfont{Noto Sans}  
\\usepackage{amsmath, amssymb}  
\\usepackage{enumitem}  
\\usepackage{tikz}  
\\pagestyle{empty}

\\begin{document}

% \--- INICIO\_SECCION: TITULO \---  
\\begin{center}  
    {\\Huge \\textbf{Jerarquía con Fracciones}} \\\\  
    \\vspace{0.5em}  
    \\hrule  
\\end{center}  
% \--- FIN\_SECCION: TITULO \---

\\vspace{1em}

% \--- INICIO\_SECCION: EJEMPLOS \---  
\\section\*{\\centering Ejemplos}

\\noindent  
\\begin{minipage}\[t\]{0.48\\textwidth}  
    \\begin{center}\\textbf{Ejemplo 1}\\end{center}  
    \\begin{align\*}  
        \\frac{1}{3} \+ \\frac{4}{5} \- \\frac{6}{3} \+ \\frac{3}{6} \- \\frac{6}{5} &= \\\\  
        \-\\frac{5}{3} \- \\frac{2}{5} \+ \\frac{3}{6} &= \\\\  
        \\frac{-50 \- 12 \+ 15}{30} &= \\mathbf{-\\frac{47}{30}}  
    \\end{align\*}

    \\begin{center}\\textbf{Ejemplo 2}\\end{center}  
    \\begin{align\*}  
        \\left(\\frac{3}{5}\\right)^2 \- 2\\left(\\frac{1}{3} \- \\frac{4}{5}\\right) \- \\frac{3}{2} &= \\\\  
        \\frac{9}{25} \- \\frac{2}{1}\\left(\\frac{5 \- 12}{15}\\right) \- \\frac{3}{2} &= \\\\  
        \\frac{9}{25} \- \\frac{2}{1}\\left(-\\frac{7}{15}\\right) \- \\frac{3}{2} &= \\\\  
        \\frac{9}{25} \+ \\frac{14}{15} \- \\frac{3}{2} &= \\\\  
        \\frac{54 \+ 140 \- 225}{150} &= \\mathbf{-\\frac{31}{150}}  
    \\end{align\*}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.48\\textwidth}  
    \\begin{center}\\textbf{Ejemplo 3}\\end{center}  
    \\begin{align\*}  
        \\frac{1}{2} \\left\[ \\frac{3}{4} \- 5 \\left(2 \- \\frac{1}{3}\\right) \\right\] &= \\\\  
        \\frac{1}{2} \\left\[ \\frac{3}{4} \- \\frac{5}{1} \\left(\\frac{6 \- 1}{3}\\right) \\right\] &= \\\\  
        \\frac{1}{2} \\left\[ \\frac{3}{4} \- \\frac{5}{1} \\left(\\frac{5}{3}\\right) \\right\] &= \\\\  
        \\frac{1}{2} \\left\[ \\frac{3}{4} \- \\frac{25}{3} \\right\] &= \\\\  
        \\frac{1}{2} \\left\[ \\frac{9 \- 100}{12} \\right\] &= \\mathbf{-\\frac{91}{24}}  
    \\end{align\*}

    \\begin{center}\\textbf{Ejemplo 4}\\end{center}  
    \\begin{align\*}  
        \\frac{\\frac{3}{2}\\left\[\\frac{1}{4}-3\\right\]^2}{\\frac{2}{5}-3\\left(\\frac{1}{4}\\right)} &= \\\\  
        \\frac{\\frac{3}{2}\\left\[\\frac{1-12}{4}\\right\]^2}{\\frac{2}{5}-\\frac{3}{4}} &= \\\\  
        \\frac{\\frac{3}{2}\\left\[\\frac{-11}{4}\\right\]^2}{\\frac{8-15}{20}} &= \\\\  
        \\frac{\\frac{3}{2}\\left\[\\frac{121}{16}\\right\]}{\\frac{-7}{20}} &= \\frac{\\frac{363}{32}}{\\frac{-7}{20}} \= \\mathbf{-\\frac{1815}{56}}  
    \\end{align\*}  
\\end{minipage}  
% \--- FIN\_SECCION: EJEMPLOS \---

\\vspace{1em}  
\\rule{\\textwidth}{0.4pt}

% \--- INICIO\_SECCION: EJERCICIOS \---  
\\section\*{\\centering Ejercicios}

\\noindent  
\\begin{minipage}\[t\]{0.48\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 1}\\end{center}  
    \\begin{itemize}\[label={}, leftmargin=0pt\]  
        \\item $\\frac{1}{4}-\\frac{6}{5}+\\frac{6}{4}+\\frac{3}{5}-\\frac{7}{10}=$  
        \\item $\\left(\\frac{1}{2}\\right)^3-4\\left(\\frac{3}{2}-\\frac{5}{6}\\right)-\\frac{1}{4}=$  
        \\item $\\frac{2}{3}\\left\[\\frac{1}{2}+4\\left(3-\\frac{2}{5}\\right)\\right\]=$  
        \\item $\\frac{\\frac{3}{5}\\left\[\\frac{1}{2}-4\\right\]^2}{\\frac{3}{2}-2\\left(\\frac{1}{6}\\right)}=$  
    \\end{itemize}

    \\vspace{2em}  
    \\begin{center}\\textbf{\\large Bloque 2}\\end{center}  
    \\begin{itemize}\[label={}, leftmargin=0pt\]  
        \\item $-\\frac{2}{4}+\\frac{6}{3}-\\frac{8}{4}-\\frac{7}{3}+\\frac{1}{6}=$  
        \\item $\\left(\\frac{2}{5}\\right)^2-\\frac{3}{5}-4\\left(\\frac{1}{2}-3\\right)=$  
        \\item $-\\frac{2}{3}\\left\[\\frac{4}{5}-6\\left(2-\\frac{1}{3}\\right)\\right\]=$  
        \\item $\\frac{\\frac{5}{3}\\left\[\\frac{1}{3}-2\\right\]^2}{\\frac{1}{5}-3\\left(\\frac{2}{6}\\right)}=$  
    \\end{itemize}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.48\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 3}\\end{center}  
    \\begin{itemize}\[label={}, leftmargin=0pt\]  
        \\item $-\\frac{8}{3}-\\frac{2}{3}+\\frac{7}{4}-\\frac{9}{4}-\\frac{3}{15}=$  
        \\item $\\frac{2}{3}-\\left(\\frac{1}{4}\\right)^2-3\\left(-\\frac{1}{2}-\\frac{3}{4}\\right)=$  
        \\item $-\\frac{4}{5}\\left\[-\\frac{2}{3}-\\frac{2}{5}\\left(\\frac{3}{4}+1\\right)\\right\]=$  
        \\item $\\frac{\\frac{3}{4}\\left\[\\frac{1}{5}-3\\right\]^2}{\\frac{5}{2}-5\\left(\\frac{2}{4}\\right)}=$  
    \\end{itemize}

    \\vspace{2em}  
    \\begin{center}\\textbf{\\large Bloque 4}\\end{center}  
    \\begin{itemize}\[label={}, leftmargin=0pt\]  
        \\item $\\frac{2}{6}-\\frac{3}{5}+\\frac{4}{2}-\\frac{3}{5}-\\frac{1}{2}=$  
        \\item $\\frac{3}{4}-\\frac{2}{5}\\left(\\frac{1}{3}-\\frac{4}{6}\\right)+\\left(\\frac{2}{3}\\right)^2=$  
        \\item $\\frac{6}{3}\\left\[4-5\\left(-\\frac{3}{2}-2\\right)\\right\]=$  
        \\item $\\frac{-\\frac{5}{6}\\left\[\\frac{1}{2}-5\\right\]^2}{\\frac{3}{4}-5\\left(\\frac{1}{10}\\right)}=$  
    \\end{itemize}  
\\end{minipage}  
% \--- FIN\_SECCION: EJERCICIOS \---

\\newpage

% \--- INICIO\_SECCION: EJERCICIOS\_RESUELTOS \---  
\\section\*{\\centering Ejercicios Resueltos}

\\noindent  
\\begin{minipage}\[t\]{0.48\\textwidth}  
    \\begin{center}\\textbf{Bloque 1}\\end{center}  
    \\begin{align\*}  
        \\frac{1}{4}-\\frac{6}{5}+\\frac{6}{4}+\\frac{3}{5}-\\frac{7}{10} &= \\\\  
        \\frac{7}{4}-\\frac{3}{5}-\\frac{7}{10} &= \\\\  
        \\frac{35-12-14}{20} &= \\mathbf{\\frac{9}{20}}  
    \\end{align\*}  
    \\begin{align\*}  
        \\left(\\frac{1}{2}\\right)^3-4\\left(\\frac{3}{2}-\\frac{5}{6}\\right)-\\frac{1}{4} &= \\\\  
        \\frac{1}{8}-4\\left(\\frac{9-5}{6}\\right)-\\frac{1}{4} &= \\\\  
        \\frac{1}{8}-\\frac{16}{6}-\\frac{1}{4} &= \\\\  
        \\frac{3-64-6}{24} &= \\mathbf{-\\frac{67}{24}}  
    \\end{align\*}  
    \\begin{align\*}  
        \\frac{2}{3}\\left\[\\frac{1}{2}+4\\left(3-\\frac{2}{5}\\right)\\right\] &= \\\\  
        \\frac{2}{3}\\left\[\\frac{1}{2}+4\\left(\\frac{13}{5}\\right)\\right\] &= \\\\  
        \\frac{2}{3}\\left\[\\frac{1}{2}+\\frac{52}{5}\\right\] &= \\\\  
        \\frac{2}{3}\\left\[\\frac{5+104}{10}\\right\] &= \\mathbf{\\frac{109}{15}}  
    \\end{align\*}  
    \\begin{align\*}  
        \\frac{\\frac{3}{5}\\left\[\\frac{1}{2}-4\\right\]^2}{\\frac{3}{2}-2\\left(\\frac{1}{6}\\right)} &= \\\\  
        \\frac{\\frac{3}{5}\\left\[-\\frac{7}{2}\\right\]^2}{\\frac{3}{2}-\\frac{2}{6}} &= \\\\  
        \\frac{\\frac{3}{5}\\left\[\\frac{49}{4}\\right\]}{\\frac{9-2}{6}} &= \\\\  
        \\frac{\\frac{147}{20}}{\\frac{7}{6}} \= \\frac{882}{140} &= \\mathbf{\\frac{63}{10}}  
    \\end{align\*}

    \\begin{center}\\textbf{Bloque 2}\\end{center}  
    \\begin{align\*}  
        \-\\frac{2}{4}+\\frac{6}{3}-\\frac{8}{4}-\\frac{7}{3}+\\frac{1}{6} &= \\\\  
        \-\\frac{10}{4}-\\frac{1}{3}+\\frac{1}{6} &= \\\\  
        \\frac{-30-4+2}{12} &= \\\\  
        \-\\frac{32}{12} &= \\mathbf{-\\frac{8}{3}}  
    \\end{align\*}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.48\\textwidth}  
    \\begin{align\*}  
        \\left(\\frac{2}{5}\\right)^2-\\frac{3}{5}-4\\left(\\frac{1}{2}-3\\right) &= \\\\  
        \\frac{4}{25}-\\frac{3}{5}-4\\left(-\\frac{5}{2}\\right) &= \\\\  
        \\frac{4}{25}-\\frac{3}{5}+10 &= \\\\  
        \\frac{8-30+500}{50} &= \\mathbf{\\frac{239}{25}}  
    \\end{align\*}  
    \\begin{align\*}  
        \-\\frac{2}{3}\\left\[\\frac{4}{5}-6\\left(2-\\frac{1}{3}\\right)\\right\] &= \\\\  
        \-\\frac{2}{3}\\left\[\\frac{4}{5}-6\\left(\\frac{5}{3}\\right)\\right\] &= \\\\  
        \-\\frac{2}{3}\\left\[\\frac{4}{5}-10\\right\] &= \\\\  
        \-\\frac{2}{3}\\left\[-\\frac{46}{5}\\right\] &= \\mathbf{\\frac{92}{15}}  
    \\end{align\*}  
    \\begin{align\*}  
        \\frac{\\frac{5}{3}\\left\[\\frac{1}{3}-2\\right\]^2}{\\frac{1}{5}-3\\left(\\frac{2}{6}\\right)} &= \\\\  
        \\frac{\\frac{5}{3}\\left\[-\\frac{5}{3}\\right\]^2}{\\frac{1}{5}-1} &= \\\\  
        \\frac{\\frac{5}{3}\\left\[\\frac{25}{9}\\right\]}{-\\frac{4}{5}} &= \\\\  
        \\frac{\\frac{125}{27}}{-\\frac{4}{5}} &= \\mathbf{-\\frac{625}{108}}  
    \\end{align\*}

    \\begin{center}\\textbf{Bloque 3}\\end{center}  
    \\begin{align\*}  
        \-\\frac{8}{3}-\\frac{2}{3}+\\frac{7}{4}-\\frac{9}{4}-\\frac{3}{15} &= \\\\  
        \-\\frac{10}{3}-\\frac{2}{4}-\\frac{3}{15} &= \\\\  
        \\frac{-200-30-12}{60} &= \\mathbf{-\\frac{121}{30}}  
    \\end{align\*}  
    \\begin{align\*}  
        \\frac{2}{3}-\\left(\\frac{1}{4}\\right)^2-3\\left(-\\frac{1}{2}-\\frac{3}{4}\\right) &= \\\\  
        \\frac{2}{3}-\\frac{1}{16}-3\\left(-\\frac{5}{4}\\right) &= \\\\  
        \\frac{2}{3}-\\frac{1}{16}+\\frac{15}{4} &= \\\\  
        \\frac{32-3+180}{48} &= \\mathbf{\\frac{209}{48}}  
    \\end{align\*}  
\\end{minipage}

\\newpage

\\noindent  
\\begin{minipage}\[t\]{0.48\\textwidth}  
    \\begin{align\*}  
        \-\\frac{4}{5}\\left\[-\\frac{2}{3}-\\frac{2}{5}\\left(\\frac{3}{4}+1\\right)\\right\] &= \\\\  
        \-\\frac{4}{5}\\left\[-\\frac{2}{3}-\\frac{2}{5}\\left(\\frac{7}{4}\\right)\\right\] &= \\\\  
        \-\\frac{4}{5}\\left\[-\\frac{2}{3}-\\frac{14}{20}\\right\] &= \\\\  
        \-\\frac{4}{5}\\left\[-\\frac{82}{60}\\right\] &= \\mathbf{\\frac{82}{75}}  
    \\end{align\*}  
    \\begin{align\*}  
        \\frac{\\frac{3}{4}\\left\[\\frac{1}{5}-3\\right\]^2}{\\frac{5}{2}-5\\left(\\frac{2}{4}\\right)} &= \\\\  
        \\frac{\\frac{3}{4}\\left\[-\\frac{14}{5}\\right\]^2}{\\frac{5}{2}-\\frac{10}{4}} &= \\\\  
        \\frac{\\frac{3}{4}\\left\[\\frac{196}{25}\\right\]}{0} &= \\mathbf{\\text{Indeterminado}}  
    \\end{align\*}

    \\begin{center}\\textbf{Bloque 4}\\end{center}  
    \\begin{align\*}  
        \\frac{2}{6}-\\frac{3}{5}+\\frac{4}{2}-\\frac{3}{5}-\\frac{1}{2} &= \\\\  
        \\frac{1}{3}-\\frac{6}{5}+\\frac{3}{2} &= \\\\  
        \\frac{10-36+45}{30} &= \\mathbf{\\frac{19}{30}}  
    \\end{align\*}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.48\\textwidth}  
    \\begin{align\*}  
        \\frac{3}{4}-\\frac{2}{5}\\left(\\frac{1}{3}-\\frac{4}{6}\\right)+\\left(\\frac{2}{3}\\right)^2 &= \\\\  
        \\frac{3}{4}-\\frac{2}{5}\\left(-\\frac{1}{3}\\right)+\\frac{4}{9} &= \\\\  
        \\frac{3}{4}+\\frac{2}{15}+\\frac{4}{9} &= \\\\  
        \\frac{135+24+80}{180} &= \\mathbf{\\frac{239}{180}}  
    \\end{align\*}  
    \\begin{align\*}  
        \\frac{6}{3}\\left\[4-5\\left(-\\frac{3}{2}-2\\right)\\right\] &= \\\\  
        2\\left\[4-5\\left(-\\frac{7}{2}\\right)\\right\] &= \\\\  
        2\\left\[4+\\frac{35}{2}\\right\] &= \\\\  
        2\\left\[\\frac{43}{2}\\right\] &= \\mathbf{43}  
    \\end{align\*}  
    \\begin{align\*}  
        \\frac{-\\frac{5}{6}\\left\[\\frac{1}{2}-5\\right\]^2}{\\frac{3}{4}-5\\left(\\frac{1}{10}\\right)} &= \\\\  
        \\frac{-\\frac{5}{6}\\left\[-\\frac{9}{2}\\right\]^2}{\\frac{3}{4}-\\frac{5}{10}} &= \\\\  
        \\frac{-\\frac{5}{6}\\left\[\\frac{81}{4}\\right\]}{\\frac{1}{4}} &= \\\\  
        \\frac{-\\frac{405}{24}}{\\frac{1}{4}} \= \-\\frac{1620}{24} &= \\mathbf{-\\frac{135}{2}}  
    \\end{align\*}  
\\end{minipage}  
% \--- FIN\_SECCION: EJERCICIOS\_RESUELTOS \---

\\vspace{1em}  
\\rule{\\textwidth}{0.4pt}

% \--- INICIO\_SECCION: EXTRAS \---  
\\section\*{\\centering Extras}

\\noindent  
\\begin{minipage}\[t\]{0.48\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 1}\\end{center}  
    \\begin{itemize}\[label={}, leftmargin=0pt\]  
        \\item $\\frac{7}{3} \+ \\frac{3}{4} \+ \\frac{6}{5} \- \\frac{8}{4} \- \\frac{2}{5} \= \\mathbf{\\frac{127}{60}}$  
        \\item $-\\frac{3}{5} \+ \\left(\\frac{2}{5}\\right)^2 \- 4\\left(-\\frac{1}{3} \- \\frac{4}{5}\\right) \= \\mathbf{\\frac{307}{75}}$  
        \\item $\\frac{5}{6} \\left\[-\\frac{3}{4} \+ \\frac{3}{6} \\left(\\frac{4}{5} \- 1\\right) \\right\] \= \\mathbf{-\\frac{17}{24}}$  
        \\item $-\\frac{4}{5} \+ \\frac{3}{2} \+ \\frac{4}{5} \+ \\frac{3}{8} \-\\frac{6}{8} \= \\mathbf{\\frac{9}{8}}$  
        \\item $-\\frac{6}{4} \+ \\frac{4}{5} \- \\frac{5}{6} \- \\frac{7}{4} \- \\frac{1}{12} \= \\mathbf{-\\frac{10}{3}}$  
        \\item $\\frac{4}{7} \+ \\left(-\\frac{3}{6}\\right)^2 \- 5\\left(-\\frac{2}{4} \+ \\frac{5}{6}\\right) \= \\mathbf{-\\frac{23}{28}}$  
        \\item $-\\frac{6}{7} \\left\[-\\frac{4}{5} \- \\frac{4}{7} \\left(\\frac{5}{6} \+ 1\\right) \\right\] \= \\mathbf{\\frac{6}{5}}$  
        \\item $\\frac{5}{8} \- \\left(\\frac{4}{7}\\right)^2 \+ 6\\left(-\\frac{3}{5} \+ \\frac{6}{7}\\right) \= \\mathbf{\\frac{717}{392}}$  
    \\end{itemize}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.48\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 2}\\end{center}  
    \\begin{itemize}\[label={}, leftmargin=0pt\]  
        \\item $\\frac{1}{2} \+ \\frac{1}{4} \- \\frac{1}{8} \= \\mathbf{\\frac{5}{8}}$  
        \\item $\\frac{3}{5} \\div \\frac{2}{3} \+ \\frac{1}{10} \= \\mathbf{1}$  
        \\item $\\left( \\frac{2}{3} \- \\frac{1}{4} \\right) \\cdot \\frac{12}{5} \= \\mathbf{1}$  
        \\item $\\frac{4}{3} \- \\left\[ \\frac{1}{2} \\cdot \\left(\\frac{1}{4} \+ \\frac{1}{3}\\right) \\right\] \= \\mathbf{\\frac{25}{24}}$  
        \\item $\\frac{\\frac{3}{4} \- \\frac{1}{2}}{\\frac{1}{8} \+ \\frac{1}{4}} \= \\mathbf{\\frac{2}{3}}$  
        \\item $\\left(\\frac{1}{2}\\right)^2 \+ \\frac{3}{4} \\cdot \\frac{1}{3} \= \\mathbf{\\frac{1}{2}}$  
        \\item $\\frac{2}{5} \\cdot \\left( \\frac{1}{2} \+ \\frac{1}{3} \\right) \- \\frac{1}{10} \= \\mathbf{\\frac{7}{30}}$  
        \\item $\\frac{5}{6} \\div \\left( 1 \- \\frac{1}{3} \\right) \+ \\frac{1}{4} \= \\mathbf{\\frac{3}{2}}$  
    \\end{itemize}  
\\end{minipage}  
% \--- FIN\_SECCION: EXTRAS \---

\\end{document}

# 2 jerarquia con fracciones

\\documentclass\[11pt\]{article}  
\\usepackage\[margin=1.5cm\]{geometry}  
\\usepackage{fontspec}  
\\setmainfont{Noto Sans}  
\\usepackage{amsmath, amssymb}  
\\usepackage{enumitem}  
\\usepackage{tikz}  
\\pagestyle{empty}

\\begin{document}

% \--- INICIO\_SECCION: TITULO \---  
\\begin{center}  
    {\\Huge \\textbf{Jerarquía con Fracciones}} \\\\  
    \\vspace{0.5em}  
    \\hrule  
\\end{center}  
% \--- FIN\_SECCION: TITULO \---

\\vspace{1em}

% \--- INICIO\_SECCION: EJEMPLOS \---  
\\section\*{\\centering Ejemplos}

\\noindent  
\\begin{minipage}\[t\]{0.48\\textwidth}  
    \\begin{center}\\textbf{Ejemplo 1}\\end{center}  
    \\begin{align\*}  
        \\frac{1}{3} \+ \\frac{4}{5} \- \\frac{6}{3} \+ \\frac{3}{6} \- \\frac{6}{5} &= \\\\  
        \-\\frac{5}{3} \- \\frac{2}{5} \+ \\frac{3}{6} &= \\\\  
        \\frac{-50 \- 12 \+ 15}{30} &= \\mathbf{-\\frac{47}{30}}  
    \\end{align\*}

    \\begin{center}\\textbf{Ejemplo 2}\\end{center}  
    \\begin{align\*}  
        \\left(\\frac{3}{5}\\right)^2 \- 2\\left(\\frac{1}{3} \- \\frac{4}{5}\\right) \- \\frac{3}{2} &= \\\\  
        \\frac{9}{25} \- \\frac{2}{1}\\left(\\frac{5 \- 12}{15}\\right) \- \\frac{3}{2} &= \\\\  
        \\frac{9}{25} \- \\frac{2}{1}\\left(-\\frac{7}{15}\\right) \- \\frac{3}{2} &= \\\\  
        \\frac{9}{25} \+ \\frac{14}{15} \- \\frac{3}{2} &= \\\\  
        \\frac{54 \+ 140 \- 225}{150} &= \\mathbf{-\\frac{31}{150}}  
    \\end{align\*}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.48\\textwidth}  
    \\begin{center}\\textbf{Ejemplo 3}\\end{center}  
    \\begin{align\*}  
        \\frac{1}{2} \\left\[ \\frac{3}{4} \- 5 \\left(2 \- \\frac{1}{3}\\right) \\right\] &= \\\\  
        \\frac{1}{2} \\left\[ \\frac{3}{4} \- \\frac{5}{1} \\left(\\frac{6 \- 1}{3}\\right) \\right\] &= \\\\  
        \\frac{1}{2} \\left\[ \\frac{3}{4} \- \\frac{5}{1} \\left(\\frac{5}{3}\\right) \\right\] &= \\\\  
        \\frac{1}{2} \\left\[ \\frac{3}{4} \- \\frac{25}{3} \\right\] &= \\\\  
        \\frac{1}{2} \\left\[ \\frac{9 \- 100}{12} \\right\] &= \\mathbf{-\\frac{91}{24}}  
    \\end{align\*}

    \\begin{center}\\textbf{Ejemplo 4}\\end{center}  
    \\begin{align\*}  
        \\frac{\\frac{3}{2}\\left\[\\frac{1}{4}-3\\right\]^2}{\\frac{2}{5}-3\\left(\\frac{1}{4}\\right)} &= \\\\  
        \\frac{\\frac{3}{2}\\left\[\\frac{1-12}{4}\\right\]^2}{\\frac{2}{5}-\\frac{3}{4}} &= \\\\  
        \\frac{\\frac{3}{2}\\left\[\\frac{-11}{4}\\right\]^2}{\\frac{8-15}{20}} &= \\\\  
        \\frac{\\frac{3}{2}\\left\[\\frac{121}{16}\\right\]}{\\frac{-7}{20}} &= \\frac{\\frac{363}{32}}{\\frac{-7}{20}} \= \\mathbf{-\\frac{1815}{56}}  
    \\end{align\*}  
\\end{minipage}  
% \--- FIN\_SECCION: EJEMPLOS \---

\\vspace{1em}  
\\rule{\\textwidth}{0.4pt}

% \--- INICIO\_SECCION: EJERCICIOS \---  
\\section\*{\\centering Ejercicios}

\\noindent  
\\begin{minipage}\[t\]{0.48\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 1}\\end{center}  
    \\begin{itemize}\[label={}, leftmargin=0pt\]  
        \\item $\\frac{1}{4}-\\frac{6}{5}+\\frac{6}{4}+\\frac{3}{5}-\\frac{7}{10}=$  
        \\item $\\left(\\frac{1}{2}\\right)^3-4\\left(\\frac{3}{2}-\\frac{5}{6}\\right)-\\frac{1}{4}=$  
        \\item $\\frac{2}{3}\\left\[\\frac{1}{2}+4\\left(3-\\frac{2}{5}\\right)\\right\]=$  
        \\item $\\frac{\\frac{3}{5}\\left\[\\frac{1}{2}-4\\right\]^2}{\\frac{3}{2}-2\\left(\\frac{1}{6}\\right)}=$  
    \\end{itemize}

    \\vspace{2em}  
    \\begin{center}\\textbf{\\large Bloque 2}\\end{center}  
    \\begin{itemize}\[label={}, leftmargin=0pt\]  
        \\item $-\\frac{2}{4}+\\frac{6}{3}-\\frac{8}{4}-\\frac{7}{3}+\\frac{1}{6}=$  
        \\item $\\left(\\frac{2}{5}\\right)^2-\\frac{3}{5}-4\\left(\\frac{1}{2}-3\\right)=$  
        \\item $-\\frac{2}{3}\\left\[\\frac{4}{5}-6\\left(2-\\frac{1}{3}\\right)\\right\]=$  
        \\item $\\frac{\\frac{5}{3}\\left\[\\frac{1}{3}-2\\right\]^2}{\\frac{1}{5}-3\\left(\\frac{2}{6}\\right)}=$  
    \\end{itemize}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.48\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 3}\\end{center}  
    \\begin{itemize}\[label={}, leftmargin=0pt\]  
        \\item $-\\frac{8}{3}-\\frac{2}{3}+\\frac{7}{4}-\\frac{9}{4}-\\frac{3}{15}=$  
        \\item $\\frac{2}{3}-\\left(\\frac{1}{4}\\right)^2-3\\left(-\\frac{1}{2}-\\frac{3}{4}\\right)=$  
        \\item $-\\frac{4}{5}\\left\[-\\frac{2}{3}-\\frac{2}{5}\\left(\\frac{3}{4}+1\\right)\\right\]=$  
        \\item $\\frac{\\frac{3}{4}\\left\[\\frac{1}{5}-3\\right\]^2}{\\frac{5}{2}-5\\left(\\frac{2}{4}\\right)}=$  
    \\end{itemize}

    \\vspace{2em}  
    \\begin{center}\\textbf{\\large Bloque 4}\\end{center}  
    \\begin{itemize}\[label={}, leftmargin=0pt\]  
        \\item $\\frac{2}{6}-\\frac{3}{5}+\\frac{4}{2}-\\frac{3}{5}-\\frac{1}{2}=$  
        \\item $\\frac{3}{4}-\\frac{2}{5}\\left(\\frac{1}{3}-\\frac{4}{6}\\right)+\\left(\\frac{2}{3}\\right)^2=$  
        \\item $\\frac{6}{3}\\left\[4-5\\left(-\\frac{3}{2}-2\\right)\\right\]=$  
        \\item $\\frac{-\\frac{5}{6}\\left\[\\frac{1}{2}-5\\right\]^2}{\\frac{3}{4}-5\\left(\\frac{1}{10}\\right)}=$  
    \\end{itemize}  
\\end{minipage}  
% \--- FIN\_SECCION: EJERCICIOS \---

\\newpage

% \--- INICIO\_SECCION: EJERCICIOS\_RESUELTOS \---  
\\section\*{\\centering Ejercicios Resueltos}

\\noindent  
\\begin{minipage}\[t\]{0.48\\textwidth}  
    \\begin{center}\\textbf{Bloque 1}\\end{center}  
    \\begin{align\*}  
        \\frac{1}{4}-\\frac{6}{5}+\\frac{6}{4}+\\frac{3}{5}-\\frac{7}{10} &= \\\\  
        \\frac{7}{4}-\\frac{3}{5}-\\frac{7}{10} &= \\\\  
        \\frac{35-12-14}{20} &= \\mathbf{\\frac{9}{20}}  
    \\end{align\*}  
    \\begin{align\*}  
        \\left(\\frac{1}{2}\\right)^3-4\\left(\\frac{3}{2}-\\frac{5}{6}\\right)-\\frac{1}{4} &= \\\\  
        \\frac{1}{8}-4\\left(\\frac{9-5}{6}\\right)-\\frac{1}{4} &= \\\\  
        \\frac{1}{8}-\\frac{16}{6}-\\frac{1}{4} &= \\\\  
        \\frac{3-64-6}{24} &= \\mathbf{-\\frac{67}{24}}  
    \\end{align\*}  
    \\begin{align\*}  
        \\frac{2}{3}\\left\[\\frac{1}{2}+4\\left(3-\\frac{2}{5}\\right)\\right\] &= \\\\  
        \\frac{2}{3}\\left\[\\frac{1}{2}+4\\left(\\frac{13}{5}\\right)\\right\] &= \\\\  
        \\frac{2}{3}\\left\[\\frac{1}{2}+\\frac{52}{5}\\right\] &= \\\\  
        \\frac{2}{3}\\left\[\\frac{5+104}{10}\\right\] &= \\mathbf{\\frac{109}{15}}  
    \\end{align\*}  
    \\begin{align\*}  
        \\frac{\\frac{3}{5}\\left\[\\frac{1}{2}-4\\right\]^2}{\\frac{3}{2}-2\\left(\\frac{1}{6}\\right)} &= \\\\  
        \\frac{\\frac{3}{5}\\left\[-\\frac{7}{2}\\right\]^2}{\\frac{3}{2}-\\frac{2}{6}} &= \\\\  
        \\frac{\\frac{3}{5}\\left\[\\frac{49}{4}\\right\]}{\\frac{9-2}{6}} &= \\\\  
        \\frac{\\frac{147}{20}}{\\frac{7}{6}} \= \\frac{882}{140} &= \\mathbf{\\frac{63}{10}}  
    \\end{align\*}

    \\begin{center}\\textbf{Bloque 2}\\end{center}  
    \\begin{align\*}  
        \-\\frac{2}{4}+\\frac{6}{3}-\\frac{8}{4}-\\frac{7}{3}+\\frac{1}{6} &= \\\\  
        \-\\frac{10}{4}-\\frac{1}{3}+\\frac{1}{6} &= \\\\  
        \\frac{-30-4+2}{12} &= \\\\  
        \-\\frac{32}{12} &= \\mathbf{-\\frac{8}{3}}  
    \\end{align\*}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.48\\textwidth}  
    \\begin{align\*}  
        \\left(\\frac{2}{5}\\right)^2-\\frac{3}{5}-4\\left(\\frac{1}{2}-3\\right) &= \\\\  
        \\frac{4}{25}-\\frac{3}{5}-4\\left(-\\frac{5}{2}\\right) &= \\\\  
        \\frac{4}{25}-\\frac{3}{5}+10 &= \\\\  
        \\frac{8-30+500}{50} &= \\mathbf{\\frac{239}{25}}  
    \\end{align\*}  
    \\begin{align\*}  
        \-\\frac{2}{3}\\left\[\\frac{4}{5}-6\\left(2-\\frac{1}{3}\\right)\\right\] &= \\\\  
        \-\\frac{2}{3}\\left\[\\frac{4}{5}-6\\left(\\frac{5}{3}\\right)\\right\] &= \\\\  
        \-\\frac{2}{3}\\left\[\\frac{4}{5}-10\\right\] &= \\\\  
        \-\\frac{2}{3}\\left\[-\\frac{46}{5}\\right\] &= \\mathbf{\\frac{92}{15}}  
    \\end{align\*}  
    \\begin{align\*}  
        \\frac{\\frac{5}{3}\\left\[\\frac{1}{3}-2\\right\]^2}{\\frac{1}{5}-3\\left(\\frac{2}{6}\\right)} &= \\\\  
        \\frac{\\frac{5}{3}\\left\[-\\frac{5}{3}\\right\]^2}{\\frac{1}{5}-1} &= \\\\  
        \\frac{\\frac{5}{3}\\left\[\\frac{25}{9}\\right\]}{-\\frac{4}{5}} &= \\\\  
        \\frac{\\frac{125}{27}}{-\\frac{4}{5}} &= \\mathbf{-\\frac{625}{108}}  
    \\end{align\*}

    \\begin{center}\\textbf{Bloque 3}\\end{center}  
    \\begin{align\*}  
        \-\\frac{8}{3}-\\frac{2}{3}+\\frac{7}{4}-\\frac{9}{4}-\\frac{3}{15} &= \\\\  
        \-\\frac{10}{3}-\\frac{2}{4}-\\frac{3}{15} &= \\\\  
        \\frac{-200-30-12}{60} &= \\mathbf{-\\frac{121}{30}}  
    \\end{align\*}  
    \\begin{align\*}  
        \\frac{2}{3}-\\left(\\frac{1}{4}\\right)^2-3\\left(-\\frac{1}{2}-\\frac{3}{4}\\right) &= \\\\  
        \\frac{2}{3}-\\frac{1}{16}-3\\left(-\\frac{5}{4}\\right) &= \\\\  
        \\frac{2}{3}-\\frac{1}{16}+\\frac{15}{4} &= \\\\  
        \\frac{32-3+180}{48} &= \\mathbf{\\frac{209}{48}}  
    \\end{align\*}  
\\end{minipage}

\\newpage

\\noindent  
\\begin{minipage}\[t\]{0.48\\textwidth}  
    \\begin{align\*}  
        \-\\frac{4}{5}\\left\[-\\frac{2}{3}-\\frac{2}{5}\\left(\\frac{3}{4}+1\\right)\\right\] &= \\\\  
        \-\\frac{4}{5}\\left\[-\\frac{2}{3}-\\frac{2}{5}\\left(\\frac{7}{4}\\right)\\right\] &= \\\\  
        \-\\frac{4}{5}\\left\[-\\frac{2}{3}-\\frac{14}{20}\\right\] &= \\\\  
        \-\\frac{4}{5}\\left\[-\\frac{82}{60}\\right\] &= \\mathbf{\\frac{82}{75}}  
    \\end{align\*}  
    \\begin{align\*}  
        \\frac{\\frac{3}{4}\\left\[\\frac{1}{5}-3\\right\]^2}{\\frac{5}{2}-5\\left(\\frac{2}{4}\\right)} &= \\\\  
        \\frac{\\frac{3}{4}\\left\[-\\frac{14}{5}\\right\]^2}{\\frac{5}{2}-\\frac{10}{4}} &= \\\\  
        \\frac{\\frac{3}{4}\\left\[\\frac{196}{25}\\right\]}{0} &= \\mathbf{\\text{Indeterminado}}  
    \\end{align\*}

    \\begin{center}\\textbf{Bloque 4}\\end{center}  
    \\begin{align\*}  
        \\frac{2}{6}-\\frac{3}{5}+\\frac{4}{2}-\\frac{3}{5}-\\frac{1}{2} &= \\\\  
        \\frac{1}{3}-\\frac{6}{5}+\\frac{3}{2} &= \\\\  
        \\frac{10-36+45}{30} &= \\mathbf{\\frac{19}{30}}  
    \\end{align\*}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.48\\textwidth}  
    \\begin{align\*}  
        \\frac{3}{4}-\\frac{2}{5}\\left(\\frac{1}{3}-\\frac{4}{6}\\right)+\\left(\\frac{2}{3}\\right)^2 &= \\\\  
        \\frac{3}{4}-\\frac{2}{5}\\left(-\\frac{1}{3}\\right)+\\frac{4}{9} &= \\\\  
        \\frac{3}{4}+\\frac{2}{15}+\\frac{4}{9} &= \\\\  
        \\frac{135+24+80}{180} &= \\mathbf{\\frac{239}{180}}  
    \\end{align\*}  
    \\begin{align\*}  
        \\frac{6}{3}\\left\[4-5\\left(-\\frac{3}{2}-2\\right)\\right\] &= \\\\  
        2\\left\[4-5\\left(-\\frac{7}{2}\\right)\\right\] &= \\\\  
        2\\left\[4+\\frac{35}{2}\\right\] &= \\\\  
        2\\left\[\\frac{43}{2}\\right\] &= \\mathbf{43}  
    \\end{align\*}  
    \\begin{align\*}  
        \\frac{-\\frac{5}{6}\\left\[\\frac{1}{2}-5\\right\]^2}{\\frac{3}{4}-5\\left(\\frac{1}{10}\\right)} &= \\\\  
        \\frac{-\\frac{5}{6}\\left\[-\\frac{9}{2}\\right\]^2}{\\frac{3}{4}-\\frac{5}{10}} &= \\\\  
        \\frac{-\\frac{5}{6}\\left\[\\frac{81}{4}\\right\]}{\\frac{1}{4}} &= \\\\  
        \\frac{-\\frac{405}{24}}{\\frac{1}{4}} \= \-\\frac{1620}{24} &= \\mathbf{-\\frac{135}{2}}  
    \\end{align\*}  
\\end{minipage}  
% \--- FIN\_SECCION: EJERCICIOS\_RESUELTOS \---

\\vspace{1em}  
\\rule{\\textwidth}{0.4pt}

% \--- INICIO\_SECCION: EXTRAS \---  
\\section\*{\\centering Extras}

\\noindent  
\\begin{minipage}\[t\]{0.48\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 1}\\end{center}  
    \\begin{itemize}\[label={}, leftmargin=0pt\]  
        \\item $\\frac{7}{3} \+ \\frac{3}{4} \+ \\frac{6}{5} \- \\frac{8}{4} \- \\frac{2}{5} \= \\mathbf{\\frac{127}{60}}$  
        \\item $-\\frac{3}{5} \+ \\left(\\frac{2}{5}\\right)^2 \- 4\\left(-\\frac{1}{3} \- \\frac{4}{5}\\right) \= \\mathbf{\\frac{307}{75}}$  
        \\item $\\frac{5}{6} \\left\[-\\frac{3}{4} \+ \\frac{3}{6} \\left(\\frac{4}{5} \- 1\\right) \\right\] \= \\mathbf{-\\frac{17}{24}}$  
        \\item $-\\frac{4}{5} \+ \\frac{3}{2} \+ \\frac{4}{5} \+ \\frac{3}{8} \-\\frac{6}{8} \= \\mathbf{\\frac{9}{8}}$  
        \\item $-\\frac{6}{4} \+ \\frac{4}{5} \- \\frac{5}{6} \- \\frac{7}{4} \- \\frac{1}{12} \= \\mathbf{-\\frac{10}{3}}$  
        \\item $\\frac{4}{7} \+ \\left(-\\frac{3}{6}\\right)^2 \- 5\\left(-\\frac{2}{4} \+ \\frac{5}{6}\\right) \= \\mathbf{-\\frac{23}{28}}$  
        \\item $-\\frac{6}{7} \\left\[-\\frac{4}{5} \- \\frac{4}{7} \\left(\\frac{5}{6} \+ 1\\right) \\right\] \= \\mathbf{\\frac{6}{5}}$  
        \\item $\\frac{5}{8} \- \\left(\\frac{4}{7}\\right)^2 \+ 6\\left(-\\frac{3}{5} \+ \\frac{6}{7}\\right) \= \\mathbf{\\frac{717}{392}}$  
    \\end{itemize}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.48\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 2}\\end{center}  
    \\begin{itemize}\[label={}, leftmargin=0pt\]  
        \\item $\\frac{1}{2} \+ \\frac{1}{4} \- \\frac{1}{8} \= \\mathbf{\\frac{5}{8}}$  
        \\item $\\frac{3}{5} \\div \\frac{2}{3} \+ \\frac{1}{10} \= \\mathbf{1}$  
        \\item $\\left( \\frac{2}{3} \- \\frac{1}{4} \\right) \\cdot \\frac{12}{5} \= \\mathbf{1}$  
        \\item $\\frac{4}{3} \- \\left\[ \\frac{1}{2} \\cdot \\left(\\frac{1}{4} \+ \\frac{1}{3}\\right) \\right\] \= \\mathbf{\\frac{25}{24}}$  
        \\item $\\frac{\\frac{3}{4} \- \\frac{1}{2}}{\\frac{1}{8} \+ \\frac{1}{4}} \= \\mathbf{\\frac{2}{3}}$  
        \\item $\\left(\\frac{1}{2}\\right)^2 \+ \\frac{3}{4} \\cdot \\frac{1}{3} \= \\mathbf{\\frac{1}{2}}$  
        \\item $\\frac{2}{5} \\cdot \\left( \\frac{1}{2} \+ \\frac{1}{3} \\right) \- \\frac{1}{10} \= \\mathbf{\\frac{7}{30}}$  
        \\item $\\frac{5}{6} \\div \\left( 1 \- \\frac{1}{3} \\right) \+ \\frac{1}{4} \= \\mathbf{\\frac{3}{2}}$  
    \\end{itemize}  
\\end{minipage}  
% \--- FIN\_SECCION: EXTRAS \---

\\end{document}

# 3 Representación de fracciones

\\documentclass\[11pt\]{article}  
\\usepackage\[margin=1.5cm\]{geometry}  
\\usepackage{fontspec}  
\\setmainfont{Noto Sans}  
\\usepackage{amsmath, amssymb}  
\\usepackage{enumitem}  
\\usepackage{tikz}  
\\pagestyle{empty}

\\begin{document}

% Título principal centrado con línea separadora  
\\begin{center}  
    {\\Huge \\textbf{Representación de Fracciones}} \\\\  
    \\vspace{0.5em}  
    \\hrule  
\\end{center}

\\vspace{1em}

% \--- INICIO\_SECCION: MINI\_APUNTE \---  
\\section\*{\\centering Mini Apunte}

Representa los diferentes números mixtos de varias formas.

\\begin{itemize}\[label={}, leftmargin=0pt, itemsep=0.5em\]  
    \\item 1\. Expresa el número mixto como una fracción impropia. Escribe también al menos dos fracciones equivalentes.  
    \\item 2\. Representación geométrica.  
    \\item 3\. Convierte el número mixto en su equivalente decimal.  
    \\item 4\. Marca y localiza el número mixto en la recta numérica.  
\\end{itemize}

% \--- FIN\_SECCION: MINI\_APUNTE \---

\\vspace{1em}  
\\rule{\\textwidth}{0.4pt}  
\\vspace{1em}

% \--- INICIO\_SECCION: EJEMPLOS \---  
\\section\*{\\centering Ejemplos}

\\begin{center}  
\\renewcommand{\\arraystretch}{2.5}  
\\begin{tabular}{|c|c|c|c|c|}  
\\hline  
\\textbf{Número Mixto} & \\textbf{Fracciones equivalentes} & \\textbf{Geométrica} & \\textbf{Decimal} & \\textbf{Recta Numérica} \\\\ \\hline  
$1 \\frac{2}{3}$ & $\\frac{5}{3} \= \\frac{10}{6} \= \\frac{15}{9}$ &   
\\begin{tikzpicture}\[scale=0.5, baseline=(current bounding box.center)\]  
    \\draw\[fill=green\] (0,0) rectangle (2,0.4);  
    \\draw\[fill=green\] (0,0.5) rectangle (2,0.9);  
    \\draw\[fill=green\] (0,1) rectangle (2,1.4);  
    \\draw (0,0) rectangle (2,1.4);  
    \\draw (0,0.46) \-- (2,0.46); \\draw (0,0.93) \-- (2,0.93);  
      
    \\begin{scope}\[xshift=2.5cm\]  
    \\draw\[fill=green\] (0,0.9) rectangle (2,1.4);  
    \\draw\[fill=green\] (0,0.45) rectangle (2,0.9);  
    \\draw (0,0) rectangle (2,1.4);  
    \\draw (0,0.46) \-- (2,0.46); \\draw (0,0.93) \-- (2,0.93);  
    \\end{scope}  
\\end{tikzpicture} & $1.6\\bar{6}$ &   
\\begin{tikzpicture}\[scale=0.8, baseline=(current bounding box.center)\]  
    \\draw\[thick\] (0,0) \-- (3,0);  
    \\foreach \\x in {0,1,2} \\draw (\\x\*1.5,0.1) \-- (\\x\*1.5,-0.1) node\[below\] {\\small \\x};  
    \\foreach \\x in {0.5, 1, 2, 2.5} \\draw\[blue\] (\\x\*0.5, 0.05) \-- (\\x\*0.5, \-0.05);  
    \\filldraw\[red\] (2.5,0) circle (2pt);  
    \\draw\[-\>, bend left\] (2.5, 0.4) to (2.5, 0.1);  
\\end{tikzpicture} \\\\ \\hline  
$1 \\frac{1}{2}$ & $\\frac{3}{2} \= \\frac{6}{4} \= \\frac{9}{6}$ &   
\\begin{tikzpicture}\[scale=0.5, baseline=(current bounding box.center)\]  
    \\draw\[fill=orange\] (0,0) rectangle (2,0.6);  
    \\draw\[fill=orange\] (0,0.7) rectangle (2,1.3);  
    \\draw (0,0) rectangle (2,1.3);  
    \\draw (0,0.65) \-- (2,0.65);  
      
    \\begin{scope}\[xshift=2.5cm\]  
    \\draw\[fill=orange\] (0,0.7) rectangle (2,1.3);  
    \\draw (0,0) rectangle (2,1.3);  
    \\draw (0,0.65) \-- (2,0.65);  
    \\end{scope}  
\\end{tikzpicture} & $1.5$ &   
\\begin{tikzpicture}\[scale=0.8, baseline=(current bounding box.center)\]  
    \\draw\[thick\] (0,0) \-- (3,0);  
    \\foreach \\x in {0,1,2} \\draw (\\x\*1.5,0.1) \-- (\\x\*1.5,-0.1) node\[below\] {\\small \\x};  
    \\draw\[blue\] (0.75, 0.05) \-- (0.75, \-0.05);  
    \\draw\[blue\] (2.25, 0.05) \-- (2.25, \-0.05);  
    \\filldraw\[red\] (2.25,0) circle (2pt);  
    \\draw\[-\>, bend left\] (2.25, 0.4) to (2.25, 0.1);  
\\end{tikzpicture} \\\\ \\hline  
\\end{tabular}  
\\end{center}

% \--- FIN\_SECCION: EJEMPLOS \---

\\vspace{1em}  
\\rule{\\textwidth}{0.4pt}  
\\vspace{1em}

% \--- INICIO\_SECCION: EJERCICIOS \---  
\\section\*{\\centering Ejercicios}

Completa la siguiente tabla con la información correspondiente para cada número mixto.

\\begin{center}  
\\renewcommand{\\arraystretch}{3.5}  
\\begin{tabular}{|c|c|c|c|c|}  
\\hline  
\\textbf{Número Mixto} & \\textbf{Fracciones equivalentes} & \\textbf{Geométrica} & \\textbf{Decimal} & \\textbf{Recta Numérica} \\\\ \\hline  
$2 \\frac{1}{4}$ & & & & \\\\ \\hline  
 & $\\frac{5}{2} \= \\frac{10}{4} \= \\frac{15}{6}$ & & & \\\\ \\hline  
 & & & $1.2$ & \\\\ \\hline  
 & & \\begin{tikzpicture}\[scale=0.4\]  
    \\draw\[fill=gray\] (0,0) rectangle (1,1); \\draw\[fill=gray\] (1,0) rectangle (2,1);  
    \\draw\[fill=gray\] (0,1) rectangle (1,2); \\draw\[fill=gray\] (1,1) rectangle (2,2);  
    \\draw (0,0) grid (2,2);  
    \\begin{scope}\[xshift=2.5cm\]  
    \\draw\[fill=gray\] (0,1) rectangle (1,2); \\draw\[fill=gray\] (1,1) rectangle (2,2);  
    \\draw (0,0) grid (2,2);  
    \\end{scope}  
    \\end{tikzpicture} & & \\\\ \\hline  
\\end{tabular}  
\\end{center}

% \--- FIN\_SECCION: EJERCICIOS \---

\\newpage

% \--- INICIO\_SECCION: RESOLUCIONES \---  
\\section\*{\\centering Resoluciones}

\\begin{center}  
\\renewcommand{\\arraystretch}{2.5}  
\\begin{tabular}{|c|c|c|c|c|}  
\\hline  
\\textbf{Número Mixto} & \\textbf{Fracciones equivalentes} & \\textbf{Geométrica} & \\textbf{Decimal} & \\textbf{Recta Numérica} \\\\ \\hline  
$2 \\frac{1}{4}$ & $\\frac{9}{4} \= \\frac{18}{8} \= \\frac{27}{12}$ &   
\\begin{tikzpicture}\[scale=0.35, baseline=(current bounding box.center)\]  
    \\foreach \\x in {0,2.5} {  
        \\draw\[fill=gray\] (\\x,0) rectangle (\\x+1,1); \\draw\[fill=gray\] (\\x+1,0) rectangle (\\x+2,1);  
        \\draw\[fill=gray\] (\\x,1) rectangle (\\x+1,2); \\draw\[fill=gray\] (\\x+1,1) rectangle (\\x+2,2);  
        \\draw (\\x,0) grid (\\x+2,2);  
    }  
    \\begin{scope}\[xshift=5cm\]  
        \\draw\[fill=gray\] (0,1) rectangle (1,2);  
        \\draw (0,0) grid (2,2);  
    \\end{scope}  
\\end{tikzpicture} & $2.25$ &   
\\begin{tikzpicture}\[scale=0.6, baseline=(current bounding box.center)\]  
    \\draw\[thick\] (0,0) \-- (4,0);  
    \\foreach \\x in {0,1,2,3} \\draw (\\x\*1.2,0.1) \-- (\\x\*1.2,-0.1) node\[below\] {\\small \\x};  
    \\filldraw\[red\] (2.7,0) circle (2pt);  
\\end{tikzpicture} \\\\ \\hline  
$2 \\frac{1}{2}$ & $\\frac{5}{2} \= \\frac{10}{4} \= \\frac{15}{6}$ &   
\\begin{tikzpicture}\[scale=0.4, baseline=(current bounding box.center)\]  
    \\draw\[fill=gray\] (0,0) rectangle (2,0.6); \\draw\[fill=gray\] (0,0.7) rectangle (2,1.3);  
    \\draw (0,0) rectangle (2,1.3); \\draw (0,0.65) \-- (2,0.65);  
    \\begin{scope}\[xshift=2.5cm\]  
    \\draw\[fill=gray\] (0,0) rectangle (2,0.6); \\draw\[fill=gray\] (0,0.7) rectangle (2,1.3);  
    \\draw (0,0) rectangle (2,1.3); \\draw (0,0.65) \-- (2,0.65);  
    \\end{scope}  
    \\begin{scope}\[xshift=5cm\]  
    \\draw\[fill=gray\] (0,0.7) rectangle (2,1.3);  
    \\draw (0,0) rectangle (2,1.3); \\draw (0,0.65) \-- (2,0.65);  
    \\end{scope}  
\\end{tikzpicture} & $2.5$ &   
\\begin{tikzpicture}\[scale=0.6, baseline=(current bounding box.center)\]  
    \\draw\[thick\] (0,0) \-- (4,0);  
    \\foreach \\x in {0,1,2,3} \\draw (\\x\*1.2,0.1) \-- (\\x\*1.2,-0.1) node\[below\] {\\small \\x};  
    \\filldraw\[red\] (3,0) circle (2pt);  
\\end{tikzpicture} \\\\ \\hline  
$1 \\frac{1}{5}$ & $\\frac{6}{5} \= \\frac{12}{10} \= \\frac{18}{15}$ &   
\\begin{tikzpicture}\[scale=0.4, baseline=(current bounding box.center)\]  
    \\foreach \\y in {0,0.3,0.6,0.9,1.2} \\draw\[fill=gray\] (0,\\y) rectangle (2,\\y+0.25);  
    \\draw (0,0) rectangle (2,1.45);  
    \\begin{scope}\[xshift=2.5cm\]  
    \\draw\[fill=gray\] (0,1.2) rectangle (2,1.45);  
    \\draw (0,0) rectangle (2,1.45);  
    \\end{scope}  
\\end{tikzpicture} & $1.2$ &   
\\begin{tikzpicture}\[scale=0.6, baseline=(current bounding box.center)\]  
    \\draw\[thick\] (0,0) \-- (4,0);  
    \\foreach \\x in {0,1,2,3} \\draw (\\x\*1.2,0.1) \-- (\\x\*1.2,-0.1) node\[below\] {\\small \\x};  
    \\filldraw\[red\] (1.44,0) circle (2pt);  
\\end{tikzpicture} \\\\ \\hline  
$1 \\frac{1}{2}$ & $\\frac{3}{2} \= \\frac{6}{4} \= \\frac{9}{6}$ &   
\\begin{tikzpicture}\[scale=0.4, baseline=(current bounding box.center)\]  
    \\draw\[fill=gray\] (0,0) rectangle (2,0.6); \\draw\[fill=gray\] (0,0.7) rectangle (2,1.3);  
    \\draw (0,0) rectangle (2,1.3); \\draw (0,0.65) \-- (2,0.65);  
    \\begin{scope}\[xshift=2.5cm\]  
    \\draw\[fill=gray\] (0,0.7) rectangle (2,1.3);  
    \\draw (0,0) rectangle (2,1.3); \\draw (0,0.65) \-- (2,0.65);  
    \\end{scope}  
\\end{tikzpicture} & $1.5$ &   
\\begin{tikzpicture}\[scale=0.6, baseline=(current bounding box.center)\]  
    \\draw\[thick\] (0,0) \-- (4,0);  
    \\foreach \\x in {0,1,2,3} \\draw (\\x\*1.2,0.1) \-- (\\x\*1.2,-0.1) node\[below\] {\\small \\x};  
    \\filldraw\[red\] (1.8,0) circle (2pt);  
\\end{tikzpicture} \\\\ \\hline  
\\end{tabular}  
\\end{center}

% \--- FIN\_SECCION: RESOLUCIONES \---

\\vspace{1em}  
\\rule{\\textwidth}{0.4pt}  
\\vspace{1em}

% \--- INICIO\_SECCION: EXTRAS \---  
\\section\*{\\centering Ejercicios Extras}

Para los siguientes números mixtos, realiza la representación completa (fracciones equivalentes, representación geométrica, decimal y recta numérica).

\\begin{center}  
\\begin{minipage}\[t\]{0.22\\textwidth}  
\\begin{itemize}  
    \\item $2 \\frac{1}{2}$  
    \\item $3 \\frac{3}{4}$  
    \\item $3 \\frac{1}{6}$  
    \\item $2 \\frac{3}{4}$  
    \\item $3 \\frac{1}{5}$  
\\end{itemize}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.22\\textwidth}  
\\begin{itemize}  
    \\item $3 \\frac{2}{5}$  
    \\item $2 \\frac{1}{3}$  
    \\item $5 \\frac{1}{4}$  
    \\item $2 \\frac{2}{5}$  
    \\item $2 \\frac{3}{5}$  
\\end{itemize}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.22\\textwidth}  
\\begin{itemize}  
    \\item $4 \\frac{1}{2}$  
    \\item $5 \\frac{2}{3}$  
    \\item $2 \\frac{5}{6}$  
    \\item $3 \\frac{1}{2}$  
    \\item $2 \\frac{4}{5}$  
\\end{itemize}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.22\\textwidth}  
\\begin{itemize}  
    \\item $5 \\frac{1}{3}$  
    \\item $4 \\frac{3}{4}$  
    \\item $4 \\frac{2}{3}$  
    \\item $3 \\frac{1}{3}$  
    \\item $3 \\frac{1}{4}$  
\\end{itemize}  
\\end{minipage}  
\\end{center}

% \--- FIN\_SECCION: EXTRAS \---

\\end{document}

# 4 algebra con fracciones

\\documentclass\[11pt\]{article}  
\\usepackage\[margin=1.5cm\]{geometry}  
\\usepackage{fontspec}  
\\setmainfont{Noto Sans}  
\\usepackage{amsmath, amssymb}  
\\usepackage{enumitem}  
\\usepackage{tikz}  
\\pagestyle{empty}

\\begin{document}

% Título principal centrado con línea separadora  
\\begin{center}  
    {\\Huge \\textbf{Álgebra con Fracciones}} \\\\  
    \\vspace{0.5em}  
    \\hrule  
\\end{center}

\\vspace{1em}

% \--- INICIO\_SECCION: MINI\_APUNTE \---  
\\section\*{\\centering Mini Apunte}  
Para trabajar con fracciones algebraicas, seguimos las leyes de los exponentes y la jerarquía de operaciones:  
\\begin{itemize}\[label={}, leftmargin=0pt\]  
    \\item \\textbf{Multiplicación:} Se realiza de forma directa. Los exponentes de letras iguales se suman: $(x^a)(x^b) \= x^{a+b}$.  
    \\item \\textbf{División:} Se puede realizar mediante el producto cruzado o la "ley de la herradura". Los exponentes se restan: $\\frac{x^a}{x^b} \= x^{a-b}$.  
    \\item \\textbf{Potencias:} Los exponentes de la base se multiplican por la potencia: $(x^a)^b \= x^{a \\cdot b}$.  
    \\item \\textbf{Raíces:} Los exponentes de la base se dividen entre el índice de la raíz: $\\sqrt\[n\]{x^a} \= x^{a \\div n}$.  
    \\item \\textbf{Jerarquía:} Primero se resuelven potencias y raíces, luego multiplicaciones y divisiones, y finalmente sumas y restas.  
\\end{itemize}  
% \--- FIN\_SECCION: MINI\_APUNTE \---

\\vspace{1em}  
\\rule{\\textwidth}{0.4pt}  
\\vspace{1em}

% \--- INICIO\_SECCION: EJEMPLOS \---  
\\section\*{\\centering Ejemplos}

\\noindent  
\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{itemize}\[label={}, leftmargin=0pt\]  
        \\item \\textbf{1. MULTIPLICACIÓN}  
        \\\[  
        \\left(\\frac{5x^8b^3}{6a^4b^2}\\right)\\left(\\frac{-4x^2b^1}{3a^5c^1}\\right) \= \\frac{-20x^{10}b^4}{18a^9b^2c^1} \= \\mathbf{\\frac{-10x^{10}b^2}{9a^9c^1}}  
        \\\]

        \\item \\textbf{2. DIVISIÓN}  
        \\\[  
        \\frac{\\dfrac{8x^7y^3a}{a^4}}{\\dfrac{6x^2}{-4a^3y}} \= \\frac{-32x^7y^4a^4}{6a^4x^2} \= \\mathbf{\\frac{-16x^5y^4}{3}}  
        \\\]

        \\item \\textbf{3. POTENCIACIÓN}  
        \\\[  
        \\left(\\frac{4x^3y^2b^6}{8x^4y^3b^2}\\right)^2 \= \\frac{16x^6y^4b^{12}}{64x^8y^6b^4} \= \\mathbf{\\frac{b^8}{4x^2y^2}}  
        \\\]

        \\item \\textbf{4. RADICACIÓN}  
        \\\[  
        \\sqrt{\\frac{25x^6y^4b^2}{36x^8}} \= \\frac{5x^3y^2b}{6x^4} \= \\mathbf{\\frac{5y^2b}{6x}}  
        \\\]  
    \\end{itemize}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{itemize}\[label={}, leftmargin=0pt\]  
        \\item \\textbf{5. JERARQUÍA (Potencia antes)}  
        \\begin{align\*}  
            \\frac{8x}{3} \- 4 \\left( \\frac{5}{x^2} \\right)^3 &= \\frac{8x}{3} \- \\frac{4}{1} \\left( \\frac{125}{x^6} \\right) \\\\  
            &= \\frac{8x}{3} \- \\frac{500}{x^6} \\\\  
            &= \\mathbf{\\frac{8x^7 \- 1500}{3x^6}}  
        \\end{align\*}

        \\item \\textbf{6. BINOMIO AL CUADRADO}  
        \\begin{align\*}  
            \\left( \\frac{3x^2}{2} \+ \\frac{8x^5}{3} \\right)^2 &= \\left( \\frac{3x^2}{2} \\right)^2 \+ 2 \\left( \\frac{3x^2}{2} \\right) \\left( \\frac{8x^5}{3} \\right) \+ \\left( \\frac{8x^5}{3} \\right)^2 \\\\  
            &= \\frac{9x^4}{4} \+ \\frac{48x^7}{6} \+ \\frac{64x^{10}}{9} \\\\  
            &= \\mathbf{\\frac{9x^4}{4} \+ 8x^7 \+ \\frac{64x^{10}}{9}}  
        \\end{align\*}  
          
        \\item \\textbf{7. SIMPLIFICACIÓN}  
        \\begin{align\*}  
            \\frac{x^2-2x-3}{x^2+5x+4} &= \\frac{(x-3)(x+1)}{(x+4)(x+1)} \\\\  
            &= \\mathbf{\\frac{x-3}{x+4}}  
        \\end{align\*}  
    \\end{itemize}  
\\end{minipage}  
% \--- FIN\_SECCION: EJEMPLOS \---

\\vspace{1em}  
\\rule{\\textwidth}{0.4pt}  
\\vspace{1em}

% \--- INICIO\_SECCION: EJERCICIOS \---  
\\section\*{\\centering Ejercicios}

\\noindent  
\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 1}\\end{center}  
    \\begin{itemize}\[label={}, leftmargin=0pt\]  
        \\item $\\left( \\frac{5x^4b}{3a^3b} \\right) \\left( \\frac{-6x^2a}{b^4} \\right) \=$  
        \\item $\\displaystyle \\frac{\\frac{3x^5y^2a}{b^3}}{\\frac{4xb^2}{-3ab}} \=$  
        \\item $\\left( \\frac{5x^2y^3b^4}{-2y^5a} \\right)^3 \=$  
        \\item $\\sqrt{\\frac{36x^{12}b^4}{4y^2a^6}} \=$  
        \\item $\\frac{7x}{2} \- 5 \\left( \\frac{2}{x^3} \\right)^2 \=$  
        \\item $\\left( \\frac{4x^2}{3} \+ \\frac{5x}{4} \\right)^2 \=$  
        \\item $\\frac{x^2+6x+5}{x^2+3x-10} \=$  
    \\end{itemize}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 2}\\end{center}  
    \\begin{itemize}\[label={}, leftmargin=0pt\]  
        \\item $\\left( \\frac{-6x^7y}{2x^5} \\right) \\left( \\frac{-5x^8y}{3bax} \\right) \=$  
        \\item $\\displaystyle \\frac{\\frac{-2x^4y^3b}{a^2}}{\\frac{5x^3b}{2a^2b}} \=$  
        \\item $\\left( \\frac{6x^3y^4}{-2y^8a^3x} \\right)^2 \=$  
        \\item $\\sqrt\[3\]{\\frac{-8x^9a^3}{125y^6}} \=$  
        \\item $\\frac{2x}{3} \- 4 \\left( \\frac{5}{x^4} \\right)^2 \=$  
        \\item $\\left( \\frac{6x^3}{2} \- \\frac{4x^2}{6} \\right)^2 \=$  
        \\item $\\frac{x^2+2x-3}{x^2-3x+2} \=$  
    \\end{itemize}  
\\end{minipage}

\\vspace{2em}

\\noindent  
\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 3}\\end{center}  
    \\begin{itemize}\[label={}, leftmargin=0pt\]  
        \\item $\\left( \\frac{-2x^5b^3}{5xb} \\right) \\left( \\frac{-2a^3x}{4b^3} \\right) \=$  
        \\item $\\displaystyle \\frac{\\frac{-4x^3ya}{b^2}}{\\frac{5xb}{6a^3}} \=$  
        \\item $\\left( \\frac{4x^3y^2a}{6x^7a} \\right)^2 \=$  
        \\item $\\sqrt{\\frac{25x^6b^8}{4y^6x^4}} \=$  
        \\item $\\frac{2x}{3} \- 6 \\left( \\frac{3}{x^4} \\right)^2 \=$  
        \\item $\\left( \\frac{5x^3}{2} \+ \\frac{4x}{3} \\right)^2 \=$  
        \\item $\\frac{x^2-6x+8}{x^2+x-20} \=$  
    \\end{itemize}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 4}\\end{center}  
    \\begin{itemize}\[label={}, leftmargin=0pt\]  
        \\item $\\left( \\frac{5x^4a^3}{2a^6} \\right) \\left( \\frac{-3x^8}{ya^2} \\right) \=$  
        \\item $\\displaystyle \\frac{\\frac{-4x^5y^3a}{2a}}{\\frac{5x^7}{10x^9y^4}} \=$  
        \\item $\\left( \\frac{-4x^6y^3}{5x^7b^3} \\right)^3 \=$  
        \\item $\\sqrt\[3\]{\\frac{64x^{12}a^6}{1000a^3}} \=$  
        \\item $\\frac{3x}{5} \- 4 \\left( \\frac{2}{x^5} \\right)^2 \=$  
        \\item $\\left( \\frac{3x^8}{2} \- \\frac{5x^4}{3} \\right)^2 \=$  
        \\item $\\frac{x^2-6x+8}{x^2+4x-12} \=$  
    \\end{itemize}  
\\end{minipage}  
% \--- FIN\_SECCION: EJERCICIOS \---

\\newpage

% \--- INICIO\_SECCION: RESOLUCIONES \---  
\\section\*{\\centering Resoluciones}

\\noindent  
\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 1}\\end{center}  
    \\begin{itemize}\[label={}, leftmargin=0pt\]  
        \\item   
        \\begin{align\*}  
            \\frac{-30x^6ba}{3a^3b^5} &= \\mathbf{\\frac{-10x^6}{a^2b^4}}  
        \\end{align\*}  
        \\item   
        \\begin{align\*}  
            \\frac{-9x^5y^2a^2b}{4b^5x} &= \\mathbf{\\frac{-9x^4y^2a^2}{4b^4}}  
        \\end{align\*}  
        \\item   
        \\begin{align\*}  
            \\frac{125x^6y^9b^{12}}{-8y^{15}a^3} &= \\mathbf{\\frac{-125x^6b^{12}}{8y^6a^3}}  
        \\end{align\*}  
        \\item   
        \\begin{align\*}  
            \\frac{6x^6b^2}{2ya^3} &= \\mathbf{\\frac{3x^6b^2}{ya^3}}  
        \\end{align\*}  
        \\item   
        \\begin{align\*}  
            \\frac{7x}{2} \- \\frac{5}{1} \\left( \\frac{4}{x^6} \\right) &= \\frac{7x}{2} \- \\frac{20}{x^6} \\\\  
            &= \\mathbf{\\frac{7x^7 \- 40}{2x^6}}  
        \\end{align\*}  
        \\item   
        \\begin{align\*}  
            \\left( \\frac{4x^2}{3} \\right)^2 \+ 2\\left( \\frac{4x^2}{3} \\right)\\left( \\frac{5x}{4} \\right) \+ \\left( \\frac{5x}{4} \\right)^2 &= \\\\  
            \\mathbf{\\frac{16x^4}{9} \+ \\frac{10x^3}{3} \+ \\frac{25x^2}{16}} &  
        \\end{align\*}  
        \\item   
        \\begin{align\*}  
            \\frac{(x+5)(x+1)}{(x+5)(x-2)} &= \\mathbf{\\frac{x+1}{x-2}}  
        \\end{align\*}  
    \\end{itemize}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 2}\\end{center}  
    \\begin{itemize}\[label={}, leftmargin=0pt\]  
        \\item   
        \\begin{align\*}  
            \\frac{30x^{15}y^2}{6x^6ba} &= \\mathbf{\\frac{5x^9y^2}{ba}}  
        \\end{align\*}  
        \\item   
        \\begin{align\*}  
            \\frac{-4x^4y^3b^2a^2}{5a^2x^3b} &= \\mathbf{\\frac{-4xy^3b}{5}}  
        \\end{align\*}  
        \\item   
        \\begin{align\*}  
            \\frac{36x^6y^8}{4y^{16}a^6x^2} &= \\mathbf{\\frac{9x^4}{y^8a^6}}  
        \\end{align\*}  
        \\item   
        \\begin{align\*}  
            \\mathbf{\\frac{-2x^3a}{5y^2}} &  
        \\end{align\*}  
        \\item   
        \\begin{align\*}  
            \\frac{2x}{3} \- \\frac{4}{1} \\left( \\frac{25}{x^8} \\right) &= \\frac{2x}{3} \- \\frac{100}{x^8} \\\\  
            &= \\mathbf{\\frac{2x^9 \- 300}{3x^8}}  
        \\end{align\*}  
        \\item   
        \\begin{align\*}  
            \\left( \\frac{6x^3}{2} \\right)^2 \+ 2\\left( \\frac{6x^3}{2} \\right)\\left( \\frac{-4x^2}{6} \\right) \+ \\left( \\frac{-4x^2}{6} \\right)^2 &= \\\\  
            \\mathbf{9x^6 \- 4x^5 \+ \\frac{4x^4}{9}} &  
        \\end{align\*}  
        \\item   
        \\begin{align\*}  
            \\frac{(x-1)(x+3)}{(x-2)(x-1)} &= \\mathbf{\\frac{x+3}{x-2}}  
        \\end{align\*}  
    \\end{itemize}  
\\end{minipage}

\\newpage

\\noindent  
\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 3}\\end{center}  
    \\begin{itemize}\[label={}, leftmargin=0pt\]  
        \\item   
        \\begin{align\*}  
            \\frac{4x^6a^3b^3}{20xb^4} &= \\mathbf{\\frac{x^5a^3}{5b}}  
        \\end{align\*}  
        \\item   
        \\begin{align\*}  
            \\frac{-24a^4x^3y}{5b^3x} &= \\mathbf{\\frac{-24a^4x^2y}{5b^3}}  
        \\end{align\*}  
        \\item   
        \\begin{align\*}  
            \\frac{16x^6y^4a^2}{36x^{14}a^2} &= \\mathbf{\\frac{4y^4}{9x^8}}  
        \\end{align\*}  
        \\item   
        \\begin{align\*}  
            \\mathbf{\\frac{5xb^4}{2y^3}} &  
        \\end{align\*}  
        \\item   
        \\begin{align\*}  
            \\frac{2x}{3} \- \\frac{6}{1} \\left( \\frac{9}{x^8} \\right) &= \\frac{2x}{3} \- \\frac{54}{x^8} \\\\  
            &= \\mathbf{\\frac{2x^9 \- 162}{3x^8}}  
        \\end{align\*}  
        \\item   
        \\begin{align\*}  
            \\mathbf{\\frac{25x^6}{4} \+ \\frac{20x^4}{3} \+ \\frac{16x^2}{9}} &  
        \\end{align\*}  
        \\item   
        \\begin{align\*}  
            \\frac{(x-4)(x-2)}{(x-4)(x+5)} &= \\mathbf{\\frac{x-2}{x+5}}  
        \\end{align\*}  
    \\end{itemize}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 4}\\end{center}  
    \\begin{itemize}\[label={}, leftmargin=0pt\]  
        \\item   
        \\begin{align\*}  
            \\frac{-15x^{12}a^3}{2a^8y} &= \\mathbf{\\frac{-15x^{12}}{2a^5y}}  
        \\end{align\*}  
        \\item   
        \\begin{align\*}  
            \\frac{-40x^{14}y^7a}{10ax^7} &= \\mathbf{-4x^7y^7}  
        \\end{align\*}  
        \\item   
        \\begin{align\*}  
            \\frac{-64x^{18}y^9}{125x^{21}b^9} &= \\mathbf{\\frac{-64y^9}{125x^3b^9}}  
        \\end{align\*}  
        \\item   
        \\begin{align\*}  
            \\frac{4x^4a^2}{10a} &= \\mathbf{\\frac{2x^4a}{5}}  
        \\end{align\*}  
        \\item   
        \\begin{align\*}  
            \\frac{3x}{5} \- \\frac{4}{1} \\left( \\frac{4}{x^{10}} \\right) &= \\frac{3x}{5} \- \\frac{16}{x^{10}} \\\\  
            &= \\mathbf{\\frac{3x^{11} \- 80}{5x^{10}}}  
        \\end{align\*}  
        \\item   
        \\begin{align\*}  
            \\mathbf{\\frac{9x^{16}}{4} \- 5x^{12} \+ \\frac{25x^8}{9}} &  
        \\end{align\*}  
        \\item   
        \\begin{align\*}  
            \\frac{(x-4)(x-2)}{(x+6)(x-2)} &= \\mathbf{\\frac{x-4}{x+6}}  
        \\end{align\*}  
    \\end{itemize}  
\\end{minipage}  
% \--- FIN\_SECCION: RESOLUCIONES \---

\\newpage

% \--- INICIO\_SECCION: EXTRAS \---  
\\section\*{\\centering Ejercicios Extras}

\\noindent  
\\begin{minipage}\[t\]{0.24\\textwidth}  
    \\begin{itemize}\[label={}, leftmargin=0pt\]  
        \\item $\\left( \\frac{7a^8}{6a^3c} \\right) \\left( \\frac{-9x^4a}{c^7} \\right) \=$  
        \\item $\\displaystyle \\frac{\\frac{6x^8y^3}{c^5}}{\\frac{8xc^4}{-7xc}} \=$  
        \\item $\\left( \\frac{2x^5y^3c^6}{-5y^9a} \\right)^3 \=$  
        \\item $\\sqrt{\\frac{81x^{14}c^6}{36c^6a^8}} \=$  
        \\item $-\\frac{10x}{6} \+ 2 \\left( \\frac{4}{x^7} \\right)^3 \=$  
        \\item $\\left( \\frac{5x^2}{7} \+ \\frac{3x}{4} \\right)^2 \=$  
        \\item $\\frac{x^2 \- 8x \+ 15}{x^2 \- x \- 20} \=$  
    \\end{itemize}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.24\\textwidth}  
    \\begin{itemize}\[label={}, leftmargin=0pt\]  
        \\item $\\left( \\frac{5a^8}{12a^2c} \\right) \\left( \\frac{-6c^3a}{c^5} \\right) \=$  
        \\item $\\displaystyle \\frac{\\frac{-x^4y^3}{3c^4}}{\\frac{7xc^3}{-5yc}} \=$  
        \\item $\\left( \\frac{6x^3y^4c^5}{-5y^8c} \\right)^3 \=$  
        \\item $\\sqrt\[3\]{\\frac{-10x^{12}c^6}{64y^3a^9}} \=$  
        \\item $-\\frac{7x}{4} \- 5 \\left( \\frac{2}{x^4} \\right)^2 \=$  
        \\item $\\left( \\frac{4x^3}{5} \- \\frac{7x}{6} \\right)^2 \=$  
        \\item $\\frac{x^2 \- 4x \+ 5}{x^2 \- 3x \- 10} \=$  
    \\end{itemize}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.24\\textwidth}  
    \\begin{itemize}\[label={}, leftmargin=0pt\]  
        \\item $\\left( \\frac{4x^3}{5a^4b} \\right) \\left( \\frac{-6x^2b}{b^6} \\right) \=$  
        \\item $\\displaystyle \\frac{\\frac{5x^6y^2}{b^5}}{\\frac{7xb^3}{-6y^3}} \=$  
        \\item $\\left( \\frac{3x^3y^5b^6}{-2y^7a} \\right)^3 \=$  
        \\item $\\sqrt{\\frac{36x^{14}b^8}{25y^4a^6}} \=$  
        \\item $\\frac{11x}{5} \- 3 \\left( \\frac{5}{x^5} \\right)^3 \=$  
        \\item $\\left( \\frac{7x^2}{8} \+ \\frac{5x}{6} \\right)^2 \=$  
        \\item $\\frac{x^2 \+ 6x \+ 9}{x^2 \- x \- 12} \=$  
    \\end{itemize}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.24\\textwidth}  
    \\begin{itemize}\[label={}, leftmargin=0pt\]  
        \\item $\\left( \\frac{5x^2}{6a^2b} \\right) \\left( \\frac{-4x^3a}{b^5} \\right) \=$  
        \\item $\\displaystyle \\frac{\\frac{7x^7y^2}{b^4}}{\\frac{3xb^3}{-5xy}} \=$  
        \\item $\\left( \\frac{4x^4y^2b^5}{-3y^6a} \\right)^3 \=$  
        \\item $\\sqrt\[3\]{\\frac{-48x^{15}a^9}{27y^6a^3}} \=$  
        \\item $\\frac{9x}{6} \- 4 \\left( \\frac{6}{x^6} \\right)^2 \=$  
        \\item $\\left( \\frac{5x^2}{7} \- \\frac{4x}{3} \\right)^2 \=$  
        \\item $\\frac{x^2 \- 7x \+ 10}{x^2 \+ 6x \- 16} \=$  
    \\end{itemize}  
\\end{minipage}  
% \--- FIN\_SECCION: EXTRAS \---

\\end{document}

# 5 ecuaciones contracciones

\\documentclass\[11pt\]{article}  
\\usepackage\[margin=1.5cm\]{geometry}  
\\usepackage{fontspec}  
\\setmainfont{Noto Sans}  
\\usepackage{amsmath, amssymb}  
\\usepackage{enumitem}  
\\usepackage{tikz}  
\\pagestyle{empty}

% Configuración para listas sin numeración ni viñetas  
\\setlist\[itemize\]{label={}, leftmargin=0pt, itemsep=1.2em}

\\begin{document}

% Título principal  
\\begin{center}  
    {\\Huge \\textbf{Ecuaciones con Fracciones}} \\\\  
    \\vspace{0.5em}  
    \\hrule  
\\end{center}

\\vspace{1em}

% \--- INICIO\_SECCION: EJEMPLOS \---  
\\section\*{\\centering Ejemplos}

\\begin{center}\\textbf{\\large Operaciones Directas con Fracciones}\\end{center}  
\\begin{itemize}  
    \\item   
    \\begin{align\*}  
        3\\left(\\frac{1}{2} \- \\frac{4}{5}x\\right) \- 5x &= \\frac{2}{5}x \+ 3 \\\\  
        \\frac{3}{2} \- \\frac{12}{5}x \- 5x &= \\frac{2}{5}x \+ 3 \\\\  
        \-\\frac{12}{5}x \- 5x \- \\frac{2}{5}x &= 3 \- \\frac{3}{2} \\\\  
        \-\\frac{14}{5}x \- 5x &= \\frac{6 \- 3}{2} \\\\  
        \\left(-\\frac{14}{5} \- 5\\right)x &= \\frac{3}{2} \\\\  
        \-\\frac{39}{5}x &= \\frac{3}{2} \\\\  
        x &= \\frac{3}{2} \\left(\\frac{5}{-39}\\right) \\\\  
        \\mathbf{x \= \\frac{15}{-78} \= \-\\frac{5}{26} \\approx \-0.19}  
    \\end{align\*}  
\\end{itemize}

\\vspace{0.5em}  
\\hrule  
\\vspace{1em}

\\begin{center}\\textbf{\\large Igualando denominador}\\end{center}  
\\begin{itemize}  
    \\item   
    \\begin{align\*}  
        \-\\frac{6}{x} \+ \\frac{4}{3x} &= \\frac{7}{5} \\\\  
        \-\\frac{18}{3x} \+ \\frac{4}{3x} &= \\frac{7}{5} \\\\  
        \\frac{-14}{3x} &= \\frac{7}{5} \\\\  
        \-14(5) &= 7(3x) \\\\  
        \-70 &= 21x \\\\  
        \\frac{-70}{21} &= x \\\\  
        \\mathbf{x \= \-\\frac{70}{21} \= \-\\frac{10}{3} \\approx \-3.33}  
    \\end{align\*}  
\\end{itemize}

\\vspace{0.5em}  
\\hrule  
\\vspace{1em}

\\begin{center}\\textbf{\\large Multiplicación por el MCM}\\end{center}  
\\begin{itemize}  
    \\item   
    \\begin{align\*}  
        \\frac{4}{2}x \- \\frac{3}{5} &= \-\\frac{1}{4}x \- \\frac{4}{3} \\\\  
        60 \\left(\\frac{4}{2}x \- \\frac{3}{5}\\right) &= 60 \\left(-\\frac{1}{4}x \- \\frac{4}{3}\\right) \\\\  
        \\frac{240}{2}x \- \\frac{180}{5} &= \-\\frac{60}{4}x \- \\frac{240}{3} \\\\  
        120x \- 36 &= \-15x \- 80 \\\\  
        120x \+ 15x &= \-80 \+ 36 \\\\  
        135x &= \-44 \\\\  
        \\mathbf{x \= \\frac{-44}{135} \\approx \-0.32}  
    \\end{align\*}  
\\end{itemize}  
% \--- FIN\_SECCION: EJEMPLOS \---

\\newpage

% \--- INICIO\_SECCION: EJERCICIOS \---  
\\section\*{\\centering Ejercicios}

\\noindent  
\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 1}\\end{center}  
    \\begin{itemize}  
        \\item $-\\frac{3}{2x} \- \\frac{4}{6x} \= \\frac{4}{5}$  
        \\item $\\frac{3}{2}x \- \\frac{2}{5} \= \-\\frac{3}{4}x \- \\frac{6}{5}$  
        \\item $2\\left(\\frac{5}{6} \+ \\frac{3}{8}x\\right) \- \\frac{2}{5}x \= 6x \- 2$  
    \\end{itemize}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 2}\\end{center}  
    \\begin{itemize}  
        \\item $-\\frac{5}{4x} \+ \\frac{2}{x} \= \-\\frac{1}{3}$  
        \\item $\\frac{3}{10}x \- \\frac{1}{5} \= \\frac{4x}{3} \- \\frac{1}{2}$  
        \\item $\\frac{5}{6}x \- 4 \= \\frac{7}{3} \- 2\\left(\\frac{1}{3} \- \\frac{5}{4}x\\right)$  
    \\end{itemize}  
\\end{minipage}

\\vspace{4em}

\\noindent  
\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 3}\\end{center}  
    \\begin{itemize}  
        \\item $-\\frac{3}{5x} \+ \\frac{2}{4x} \= \-\\frac{1}{10}$  
        \\item $-\\frac{2}{3} \+ \\frac{4}{5}x \= \-\\frac{2}{3}x \+ \\frac{5}{2}$  
        \\item $-\\frac{3}{2}x \- 4\\left(\\frac{5}{3} \- 3x\\right) \= \-\\frac{4}{2}x \- \\frac{6}{5}$  
    \\end{itemize}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 4}\\end{center}  
    \\begin{itemize}  
        \\item $-\\frac{6}{3x} \+ \\frac{2}{4x} \= \-\\frac{1}{2}$  
        \\item $\\frac{2}{6} \- \\frac{1}{2}x \= \\frac{5}{3} \- \\frac{3}{4}x$  
        \\item $\\frac{3}{4} \- \\frac{5}{2}x \= \\frac{3}{5} \- 4\\left(\\frac{2}{5}x \- \\frac{1}{2}\\right)$  
    \\end{itemize}  
\\end{minipage}  
% \--- FIN\_SECCION: EJERCICIOS \---

\\newpage

% \--- INICIO\_SECCION: EJERCICIOS RESUELTOS \---  
\\section\*{\\centering Ejercicios Resueltos}

\\begin{center}\\textbf{\\large Bloque 1}\\end{center}  
\\begin{itemize}  
    \\item   
    \\begin{align\*}  
        \-\\frac{3}{2x} \- \\frac{4}{6x} &= \\frac{4}{5} \\\\  
        \-\\frac{9}{6x} \- \\frac{4}{6x} &= \\frac{4}{5} \\\\  
        \\frac{-13}{6x} &= \\frac{4}{5} \\\\  
        \-65 &= 24x \\\\  
        \\mathbf{x \= \-\\frac{65}{24} \\approx \-2.71}  
    \\end{align\*}  
    \\item   
    \\begin{align\*}  
        \\frac{3}{2}x \- \\frac{2}{5} &= \-\\frac{3}{4}x \- \\frac{6}{5} \\\\  
        20\\left(\\frac{3}{2}x \- \\frac{2}{5}\\right) &= 20\\left(-\\frac{3}{4}x \- \\frac{6}{5}\\right) \\\\  
        30x \- 8 &= \-15x \- 24 \\\\  
        45x &= \-16 \\\\  
        \\mathbf{x \= \-\\frac{16}{45} \\approx \-0.36}  
    \\end{align\*}  
    \\item   
    \\begin{align\*}  
        2\\left(\\frac{5}{6} \+ \\frac{3}{8}x\\right) \- \\frac{2}{5}x &= 6x \- 2 \\\\  
        \\frac{5}{3} \+ \\frac{3}{4}x \- \\frac{2}{5}x &= 6x \- 2 \\\\  
        60 \\left(\\frac{5}{3} \+ \\frac{3}{4}x \- \\frac{2}{5}x\\right) &= 60(6x \- 2\) \\\\  
        100 \+ 45x \- 24x &= 360x \- 120 \\\\  
        339x &= 220 \\\\  
        \\mathbf{x \= \\frac{220}{339} \\approx 0.65}  
    \\end{align\*}  
\\end{itemize}

\\newpage

\\begin{center}\\textbf{\\large Bloque 2}\\end{center}  
\\begin{itemize}  
    \\item   
    \\begin{align\*}  
        \-\\frac{5}{4x} \+ \\frac{2}{x} &= \-\\frac{1}{3} \\\\  
        \-\\frac{5}{4x} \+ \\frac{8}{4x} &= \-\\frac{1}{3} \\\\  
        \\frac{3}{4x} &= \-\\frac{1}{3} \\\\  
        9 &= \-4x \\\\  
        \\mathbf{x \= \-\\frac{9}{4} \= \-2.25}  
    \\end{align\*}  
    \\item   
    \\begin{align\*}  
        \\frac{3}{10}x \- \\frac{1}{5} &= \\frac{4x}{3} \- \\frac{1}{2} \\\\  
        30\\left(\\frac{3}{10}x \- \\frac{1}{5}\\right) &= 30\\left(\\frac{4x}{3} \- \\frac{1}{2}\\right) \\\\  
        9x \- 6 &= 40x \- 15 \\\\  
        31x &= 9 \\\\  
        \\mathbf{x \= \\frac{9}{31} \\approx 0.29}  
    \\end{align\*}  
    \\item   
    \\begin{align\*}  
        \\frac{5}{6}x \- 4 &= \\frac{7}{3} \- 2\\left(\\frac{1}{3} \- \\frac{5}{4}x\\right) \\\\  
        \\frac{5}{6}x \- 4 &= \\frac{7}{3} \- \\frac{2}{3} \+ \\frac{5}{2}x \\\\  
        6\\left(\\frac{5}{6}x \- 4\\right) &= 6\\left(\\frac{5}{3} \+ \\frac{5}{2}x\\right) \\\\  
        5x \- 24 &= 10 \+ 15x \\\\  
        \-10x &= 34 \\\\  
        \\mathbf{x \= \-3.4}  
    \\end{align\*}  
\\end{itemize}

\\newpage

\\begin{center}\\textbf{\\large Bloque 3}\\end{center}  
\\begin{itemize}  
    \\item   
    \\begin{align\*}  
        \-\\frac{3}{5x} \+ \\frac{2}{4x} &= \-\\frac{1}{10} \\\\  
        \-\\frac{6}{10x} \+ \\frac{5}{10x} &= \-\\frac{1}{10} \\\\  
        \\frac{-1}{10x} &= \-\\frac{1}{10} \\\\  
        \-10 &= \-10x \\\\  
        \\mathbf{x \= 1}  
    \\end{align\*}  
    \\item   
    \\begin{align\*}  
        \-\\frac{2}{3} \+ \\frac{4}{5}x &= \-\\frac{2}{3}x \+ \\frac{5}{2} \\\\  
        30 \\left(-\\frac{2}{3} \+ \\frac{4}{5}x\\right) &= 30 \\left(-\\frac{2}{3}x \+ \\frac{5}{2}\\right) \\\\  
        \-20 \+ 24x &= \-20x \+ 75 \\\\  
        44x &= 95 \\\\  
        \\mathbf{x \= \\frac{95}{44} \\approx 2.16}  
    \\end{align\*}  
    \\item   
    \\begin{align\*}  
        \-\\frac{3}{2}x \- 4\\left(\\frac{5}{3} \- 3x\\right) &= \-\\frac{4}{2}x \- \\frac{6}{5} \\\\  
        \-\\frac{3}{2}x \- \\frac{20}{3} \+ 12x &= \-2x \- \\frac{6}{5} \\\\  
        30\\left(-\\frac{3}{2}x \- \\frac{20}{3} \+ 12x\\right) &= 30\\left(-2x \- \\frac{6}{5}\\right) \\\\  
        \-45x \- 200 \+ 360x &= \-60x \- 36 \\\\  
        375x &= 164 \\\\  
        \\mathbf{x \= \\frac{164}{375} \\approx 0.44}  
    \\end{align\*}  
\\end{itemize}

\\newpage

\\begin{center}\\textbf{\\large Bloque 4}\\end{center}  
\\begin{itemize}  
    \\item   
    \\begin{align\*}  
        \-\\frac{6}{3x} \+ \\frac{2}{4x} &= \-\\frac{1}{2} \\\\  
        \\frac{-8}{4x} \+ \\frac{2}{4x} &= \-\\frac{1}{2} \\\\  
        \\frac{-6}{4x} &= \-\\frac{1}{2} \\\\  
        \-12 &= \-4x \\\\  
        \\mathbf{x \= 3}  
    \\end{align\*}  
    \\item   
    \\begin{align\*}  
        \\frac{2}{6} \- \\frac{1}{2}x &= \\frac{5}{3} \- \\frac{3}{4}x \\\\  
        12 \\left(\\frac{1}{3} \- \\frac{1}{2}x\\right) &= 12 \\left(\\frac{5}{3} \- \\frac{3}{4}x\\right) \\\\  
        4 \- 6x &= 20 \- 9x \\\\  
        3x &= 16 \\\\  
        \\mathbf{x \= \\frac{16}{3} \\approx 5.33}  
    \\end{align\*}  
    \\item   
    \\begin{align\*}  
        \\frac{3}{4} \- \\frac{5}{2}x &= \\frac{3}{5} \- 4\\left(\\frac{2}{5}x \- \\frac{1}{2}\\right) \\\\  
        \\frac{3}{4} \- \\frac{5}{2}x &= \\frac{3}{5} \- \\frac{8}{5}x \+ 2 \\\\  
        20\\left(\\frac{3}{4} \- \\frac{5}{2}x\\right) &= 20\\left(\\frac{3}{5} \- \\frac{8}{5}x \+ 2\\right) \\\\  
        15 \- 50x &= 12 \- 32x \+ 40 \\\\  
        \-18x &= 37 \\\\  
        \\mathbf{x \= \-\\frac{37}{18} \\approx \-2.06}  
    \\end{align\*}  
\\end{itemize}  
% \--- FIN\_SECCION: EJERCICIOS RESUELTOS \---

\\newpage

% \--- INICIO\_SECCION: EXTRAS \---  
\\section\*{\\centering Extras}

\\noindent  
\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 1}\\end{center}  
    \\begin{itemize}  
        \\item $-\\frac{4}{3x} \- \\frac{5}{6x} \= \\frac{3}{4}$  
        \\item $\\frac{5}{3}x \- \\frac{2}{7} \= \-\\frac{3}{5}x \- \\frac{4}{6}$  
        \\item $2\\left(\\frac{4}{5} \+ \\frac{2}{7}x\\right) \- \\frac{3}{5}x \= 5x \- 1$  
    \\end{itemize}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 2}\\end{center}  
    \\begin{itemize}  
        \\item $-\\frac{5}{6x} \+ \\frac{3}{x} \= \-\\frac{2}{5}$  
        \\item $\\frac{2}{9}x \- \\frac{3}{5} \= \\frac{3x}{4} \- \\frac{2}{5}$  
        \\item $\\frac{3}{4}x \- 5 \= \\frac{6}{5} \- 2\\left(\\frac{2}{3} \- \\frac{4}{5}x\\right)$  
    \\end{itemize}  
\\end{minipage}

\\vspace{4em}

\\noindent  
\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 3}\\end{center}  
    \\begin{itemize}  
        \\item $-\\frac{4}{7x} \+ \\frac{3}{5x} \= \-\\frac{2}{9}$  
        \\item $-\\frac{3}{5} \+ \\frac{4}{6}x \= \-\\frac{3}{5}x \+ \\frac{2}{3}$  
        \\item $-\\frac{5}{3}x \- 3\\left(\\frac{4}{3} \- 2x\\right) \= \-\\frac{2}{4}x \- \\frac{5}{6}$  
    \\end{itemize}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 4}\\end{center}  
    \\begin{itemize}  
        \\item $-\\frac{2}{5x} \+ \\frac{1}{2x} \= \-\\frac{3}{10}$  
        \\item $\\frac{4}{3}x \- \\frac{1}{2} \= \\frac{2}{5}x \+ \\frac{3}{10}$  
        \\item $\\frac{2}{3} \- \\frac{4}{5}x \= \\frac{3}{6} \- 4\\left(\\frac{3}{7}x \- \\frac{2}{5}\\right)$  
    \\end{itemize}  
\\end{minipage}  
% \--- FIN\_SECCION: EXTRAS \---

\\end{document}

# 6 grafica de una ecuacion quadratica

\\documentclass\[11pt\]{article}  
\\usepackage\[margin=1.5cm\]{geometry}  
\\usepackage{fontspec}  
\\setmainfont{Noto Sans}  
\\usepackage{amsmath, amssymb}  
\\usepackage{enumitem}  
\\usepackage{tikz}  
\\pagestyle{empty}

% Configuración para listas sin viñetas  
\\setlist\[itemize\]{label={}, leftmargin=0pt, itemsep=1em}

\\begin{document}

% Título principal centrado con línea separadora  
\\begin{center}  
    {\\Huge \\textbf{Funciones Cuadráticas}} \\\\  
    \\vspace{0.5em}  
    \\hrule  
\\end{center}

\\vspace{1em}

% \--- INICIO\_SECCION: MINI\_APUNTE \---  
\\section\*{\\centering Mini Apunte}  
Una función cuadrática es de la forma $f(x) \= ax^2 \+ bx \+ c$. Para graficarla en un intervalo dado, construimos una tabla de valores calculando la imagen de cada entero en dicho intervalo. La representación gráfica es una parábola. Si $a \> 0$, la parábola abre hacia arriba; si $a \< 0$, abre hacia abajo.  
% \--- FIN\_SECCION: MINI\_APUNTE \---

\\vspace{1em}  
\\rule{\\textwidth}{0.4pt}  
\\vspace{1em}

% \--- INICIO\_SECCION: EJEMPLOS \---  
\\section\*{\\centering Ejemplos}

\\noindent  
\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\textbf{Gráfica la función:} $f(x) \= x^2 \- 6x \+ 5$ \\\\  
    \\textbf{En el intervalo:} $f: \[0, 6\] \\to \\mathbb{R}$

    \\vspace{1em}  
    \\begin{tabular}{|c|c|}  
        \\hline  
        $x$ & $f(x)$ \\\\ \\hline  
        0 & 5 \\\\ \\hline  
        1 & 0 \\\\ \\hline  
        2 & \-3 \\\\ \\hline  
        3 & \-4 \\\\ \\hline  
        4 & \-3 \\\\ \\hline  
        5 & 0 \\\\ \\hline  
        6 & 5 \\\\ \\hline  
    \\end{tabular}  
      
    \\vspace{1em}  
    \\begin{align\*}  
        f(0) &= (0)^2 \- 6(0) \+ 5 \= 5 \\\\  
        f(1) &= (1)^2 \- 6(1) \+ 5 \= 1 \- 6 \+ 5 \= 0 \\\\  
        f(2) &= (2)^2 \- 6(2) \+ 5 \= 4 \- 12 \+ 5 \= \-3 \\\\  
        f(3) &= (3)^2 \- 6(3) \+ 5 \= 9 \- 18 \+ 5 \= \-4 \\\\  
        f(4) &= (4)^2 \- 6(4) \+ 5 \= 16 \- 24 \+ 5 \= \-3 \\\\  
        f(5) &= (5)^2 \- 6(5) \+ 5 \= 25 \- 30 \+ 5 \= 0 \\\\  
        f(6) &= (6)^2 \- 6(6) \+ 5 \= 36 \- 36 \+ 5 \= 5  
    \\end{align\*}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\centering  
    \\begin{tikzpicture}\[scale=0.6\]  
        \\draw\[very thin, gray\!30\] (-1,-5) grid (7,6);  
        \\draw\[-\>, ultra thick\] (-1,0) \-- (7,0) node\[right\] {$x$};  
        \\draw\[-\>, ultra thick\] (0,-5) \-- (0,6) node\[above\] {$f(x)$};  
        \\foreach \\x in {1,2,3,4,5,6} \\draw (\\x,0.1) \-- (\\x,-0.1) node\[below\] {\\tiny \\x};  
        \\foreach \\y in {-4,-2,2,4} \\draw (0.1,\\y) \-- (-0.1,\\y) node\[left\] {\\tiny \\y};  
        \\draw\[domain=0:6, smooth, variable=\\x, red, ultra thick\] plot ({\\x}, {\\x\*\\x \- 6\*\\x \+ 5});  
        \\foreach \\p in {(0,5), (1,0), (2,-3), (3,-4), (4,-3), (5,0), (6,5)}  
            \\fill\[red\] \\p circle (4pt);  
    \\end{tikzpicture}  
\\end{minipage}  
% \--- FIN\_SECCION: EJEMPLOS \---

\\vspace{1em}  
\\rule{\\textwidth}{0.4pt}  
\\vspace{1em}

% \--- INICIO\_SECCION: EJERCICIOS \---  
\\section\*{\\centering Ejercicios}

\\begin{center}\\textbf{\\large Bloque 1}\\end{center}  
\\begin{itemize}  
    \\item $f(x) \= x^2 \- 2x \- 8, \\quad f: \[-2, 4\] \\to \\mathbb{R}$  
    \\item $f(x) \= x^2 \- 6x \+ 8, \\quad f: \[0, 7\] \\to \\mathbb{R}$  
    \\item $f(x) \= x^2 \+ 4x, \\quad f: \[-5, 1\] \\to \\mathbb{R}$  
    \\item $f(x) \= \-x^2 \- 4x, \\quad f: \[-5, 1\] \\to \\mathbb{R}$  
    \\item $f(x) \= \-x^2 \+ 2x \+ 8, \\quad f: \[-2, 4\] \\to \\mathbb{R}$  
\\end{itemize}

\\begin{center}\\textbf{\\large Bloque 2}\\end{center}  
\\begin{itemize}  
    \\item $f(x) \= \-x^2 \- 10x \- 24, \\quad f: \[-8, \-2\] \\to \\mathbb{R}$  
    \\item $f(x) \= x^2 \- 4x \+ 4, \\quad f: \[-1, 5\] \\to \\mathbb{R}$  
    \\item $f(x) \= x^2 \+ 6x \+ 9, \\quad f: \[-6, 0\] \\to \\mathbb{R}$  
    \\item $f(x) \= \-x^2 \+ 4x \- 3, \\quad f: \[-1, 5\] \\to \\mathbb{R}$  
    \\item $f(x) \= x^2 \- 7x \+ 10, \\quad f: \[-6, 3\] \\to \\mathbb{R}$  
\\end{itemize}  
% \--- FIN\_SECCION: EJERCICIOS \---

\\newpage

% \--- INICIO\_SECCION: RESOLUCIONES \---  
\\section\*{\\centering Ejercicios Resueltos}

\\begin{center}\\textbf{\\large Bloque 1}\\end{center}

\\noindent  
\\begin{minipage}\[t\]{0.45\\textwidth}  
    $f(x) \= x^2 \- 2x \- 8, \\quad \[-2, 4\]$  
      
    \\vspace{0.5em}  
    \\begin{tabular}{|c|c|}  
        \\hline $x$ & $f(x)$ \\\\ \\hline  
        \-2 & 0 \\\\ \\hline  
        \-1 & \-5 \\\\ \\hline  
        0 & \-8 \\\\ \\hline  
        1 & \-9 \\\\ \\hline  
        2 & \-8 \\\\ \\hline  
        3 & \-5 \\\\ \\hline  
        4 & 0 \\\\ \\hline  
    \\end{tabular}

    \\vspace{1em}  
    \\begin{align\*}  
        f(-2) &= (-2)^2 \- 2(-2) \- 8 \= 4 \+ 4 \- 8 \= 0 \\\\  
        f(-1) &= (-1)^2 \- 2(-1) \- 8 \= 1 \+ 2 \- 8 \= \-5 \\\\  
        f(0) &= (0)^2 \- 2(0) \- 8 \= 0 \- 0 \- 8 \= \-8 \\\\  
        f(1) &= (1)^2 \- 2(1) \- 8 \= 1 \- 2 \- 8 \= \-9 \\\\  
        f(2) &= (2)^2 \- 2(2) \- 8 \= 4 \- 4 \- 8 \= \-8 \\\\  
        f(3) &= (3)^2 \- 2(3) \- 8 \= 9 \- 6 \- 8 \= \-5 \\\\  
        f(4) &= (4)^2 \- 2(4) \- 8 \= 16 \- 8 \- 8 \= 0  
    \\end{align\*}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\centering  
    \\begin{tikzpicture}\[scale=0.5\]  
        \\draw\[very thin, gray\!30\] (-3,-10) grid (5,2);  
        \\draw\[-\>, ultra thick\] (-3,0) \-- (5,0) node\[right\] {$x$};  
        \\draw\[-\>, ultra thick\] (0,-10) \-- (0,2) node\[above\] {$f(x)$};  
        \\draw\[domain=-2:4, smooth, variable=\\x, blue, ultra thick\] plot ({\\x}, {\\x\*\\x \- 2\*\\x \- 8});  
        \\foreach \\p in {(-2,0), (-1,-5), (0,-8), (1,-9), (2,-8), (3,-5), (4,0)}  
            \\fill\[blue\] \\p circle (4pt);  
    \\end{tikzpicture}  
\\end{minipage}

\\vspace{2em}

\\noindent  
\\begin{minipage}\[t\]{0.45\\textwidth}  
    $f(x) \= x^2 \+ 4x, \\quad \[-5, 1\]$  
      
    \\vspace{0.5em}  
    \\begin{tabular}{|c|c|}  
        \\hline $x$ & $f(x)$ \\\\ \\hline  
        \-5 & 5 \\\\ \\hline  
        \-4 & 0 \\\\ \\hline  
        \-3 & \-3 \\\\ \\hline  
        \-2 & \-4 \\\\ \\hline  
        \-1 & \-3 \\\\ \\hline  
        0 & 0 \\\\ \\hline  
        1 & 5 \\\\ \\hline  
    \\end{tabular}

    \\vspace{1em}  
    \\begin{align\*}  
        f(-5) &= (-5)^2 \+ 4(-5) \= 25 \- 20 \= 5 \\\\  
        f(-4) &= (-4)^2 \+ 4(-4) \= 16 \- 16 \= 0 \\\\  
        f(-3) &= (-3)^2 \+ 4(-3) \= 9 \- 12 \= \-3 \\\\  
        f(-2) &= (-2)^2 \+ 4(-2) \= 4 \- 8 \= \-4 \\\\  
        f(-1) &= (-1)^2 \+ 4(-1) \= 1 \- 4 \= \-3 \\\\  
        f(0) &= (0)^2 \+ 4(0) \= 0 \+ 0 \= 0 \\\\  
        f(1) &= (1)^2 \+ 4(1) \= 1 \+ 4 \= 5  
    \\end{align\*}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\centering  
    \\begin{tikzpicture}\[scale=0.5\]  
        \\draw\[very thin, gray\!30\] (-6,-5) grid (2,6);  
        \\draw\[-\>, ultra thick\] (-6,0) \-- (2,0) node\[right\] {$x$};  
        \\draw\[-\>, ultra thick\] (0,-5) \-- (0,6) node\[above\] {$f(x)$};  
        \\draw\[domain=-5:1, smooth, variable=\\x, purple, ultra thick\] plot ({\\x}, {\\x\*\\x \+ 4\*\\x});  
        \\foreach \\p in {(-5,5), (-4,0), (-3,-3), (-2,-4), (-1,-3), (0,0), (1,5)}  
            \\fill\[purple\] \\p circle (4pt);  
    \\end{tikzpicture}  
\\end{minipage}

% \--- FIN\_SECCION: RESOLUCIONES \---

\\newpage

% \--- INICIO\_SECCION: EXTRAS \---  
\\section\*{\\centering Ejercicios Extras}

\\noindent  
\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 1}\\end{center}  
    \\begin{itemize}  
        \\item $f(x) \= x^2 \- x \- 2, \\quad \[-2, 3\]$  
        \\item $f(x) \= \-x^2 \+ 9, \\quad \[-4, 4\]$  
        \\item $f(x) \= x^2 \- 4x \+ 3, \\quad \[0, 4\]$  
    \\end{itemize}

    \\begin{center}\\textbf{\\large Bloque 2}\\end{center}  
    \\begin{itemize}  
        \\item $f(x) \= 2x^2 \- 4x, \\quad \[-1, 3\]$  
        \\item $f(x) \= \-x^2 \- 2x \+ 3, \\quad \[-4, 2\]$  
        \\item $f(x) \= x^2 \+ 2x \+ 1, \\quad \[-3, 1\]$  
    \\end{itemize}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 3}\\end{center}  
    \\begin{itemize}  
        \\item $f(x) \= \-2x^2 \+ 8, \\quad \[-3, 3\]$  
        \\item $f(x) \= x^2 \- 9, \\quad \[-4, 4\]$  
        \\item $f(x) \= \-x^2 \+ 6x \- 8, \\quad \[1, 5\]$  
    \\end{itemize}

    \\begin{center}\\textbf{\\large Bloque 4}\\end{center}  
    \\begin{itemize}  
        \\item $f(x) \= x^2 \+ 5x \+ 6, \\quad \[-5, 0\]$  
        \\item $f(x) \= \-x^2 \+ x \+ 6, \\quad \[-3, 4\]$  
        \\item $f(x) \= x^2 \- 2x \+ 1, \\quad \[-1, 3\]$  
    \\end{itemize}  
\\end{minipage}  
% \--- FIN\_SECCION: EXTRAS \---

\\end{document}

# 7 Ecuacion de la recta dado dos puntos

\\documentclass\[11pt\]{article}  
\\usepackage\[margin=1.5cm\]{geometry}  
\\usepackage{fontspec}  
\\setmainfont{Noto Sans}  
\\usepackage{amsmath, amssymb}  
\\usepackage{enumitem}  
\\usepackage{tikz}  
\\pagestyle{empty}

% Configuración para listas sin viñetas  
\\setlist\[itemize\]{label={}, leftmargin=0pt, itemsep=1.1em}

\\begin{document}

% Título principal centrado con línea separadora  
\\begin{center}  
    {\\Huge \\textbf{Ecuación de la Recta}} \\\\  
    \\vspace{0.5em}  
    \\hrule  
\\end{center}

\\vspace{1em}

% \--- INICIO\_SECCION: MINI\_APUNTE \---  
\\section\*{\\centering Mini Apunte}  
Para encontrar la ecuación de una recta que pasa por dos puntos $A(x\_1, y\_1)$ y $B(x\_2, y\_2)$, utilizamos la fórmula de la pendiente igualada en ambos puntos:  
\\begin{center}  
    $\\dfrac{x \- (x\_1)}{(x\_2) \- (x\_1)} \= \\dfrac{y \- (y\_1)}{(y\_2) \- (y\_1)}$  
\\end{center}  
Una vez obtenida la ecuación general $Ax \+ By \+ C \= 0$, realizamos la comprobación sustituyendo las coordenadas de los puntos originales para verificar que la igualdad se cumple.  
% \--- FIN\_SECCION: MINI\_APUNTE \---

\\vspace{1em}  
\\rule{\\textwidth}{0.4pt}  
\\vspace{1em}

% \--- INICIO\_SECCION: EJEMPLOS \---  
\\section\*{\\centering Ejemplo}

\\noindent  
\\begin{minipage}\[t\]{0.55\\textwidth}  
    \\textbf{Puntos:} $A=(-3, 2), \\quad B=(1, 4)$  
      
    \\vspace{1em}  
    \\textbf{Sustituir:}  
    \\begin{align\*}  
        \\dfrac{x \- (-3)}{(1) \- (-3)} &= \\dfrac{y \- (2)}{(4) \- (2)} \\\\  
        \\dfrac{x \+ 3}{1 \+ 3} &= \\dfrac{y \- 2}{2} \\\\  
        \\dfrac{x \+ 3}{4} &= \\dfrac{y \- 2}{2} \\\\  
        2(x \+ 3\) &= 4(y \- 2\) \\\\  
        2x \+ 6 &= 4y \- 8 \\\\  
        2x \- 4y \+ 6 \+ 8 &= 0 \\\\  
        \\mathbf{2x \- 4y \+ 14 \= 0}  
    \\end{align\*}

    \\textbf{Comprobación:} \\\\  
    \\begin{minipage}\[t\]{0.48\\linewidth}  
        $A(-3, 2)$  
        \\begin{align\*}  
            2(-3) \- 4(2) \+ 14 &= 0 \\\\  
            \-6 \- 8 \+ 14 &= 0 \\\\  
            \-14 \+ 14 &= 0 \\\\  
            0 &= 0  
        \\end{align\*}  
    \\end{minipage}  
    \\hfill  
    \\begin{minipage}\[t\]{0.48\\linewidth}  
        $B(1, 4)$  
        \\begin{align\*}  
            2(1) \- 4(4) \+ 14 &= 0 \\\\  
            2 \- 16 \+ 14 &= 0 \\\\  
            16 \- 16 &= 0 \\\\  
            0 &= 0  
        \\end{align\*}  
    \\end{minipage}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.40\\textwidth}  
    \\centering  
    \\begin{tikzpicture}\[scale=0.6\]  
        \\draw\[very thin, gray\!30\] (-5,-1) grid (3,6);  
        \\draw\[-\>, ultra thick\] (-5,0) \-- (3,0) node\[right\] {$x$};  
        \\draw\[-\>, ultra thick\] (0,-1) \-- (0,6) node\[above\] {$y$};  
        \\draw\[domain=-4.5:2, smooth, variable=\\x, blue, ultra thick\] plot ({\\x}, {0.5\*\\x \+ 3.5});  
        \\fill\[black\] (-3,2) circle (4pt) node\[above left\] {$A$};  
        \\fill\[black\] (1,4) circle (4pt) node\[above right\] {$B$};  
    \\end{tikzpicture}  
\\end{minipage}  
% \--- FIN\_SECCION: EJEMPLOS \---

\\vspace{1em}  
\\rule{\\textwidth}{0.4pt}  
\\vspace{1em}

% \--- INICIO\_SECCION: EJERCICIOS \---  
\\section\*{\\centering Ejercicios}

\\begin{center}\\textbf{\\large Bloque 1}\\end{center}  
\\begin{center}  
\\begin{minipage}\[t\]{0.8\\textwidth}  
    \\begin{itemize}  
        \\item $A=(-4, 7), \\quad B=(2, 3)$  
        \\item $A=(3, \-2), \\quad B=(-2, \-3)$  
        \\item $A=(-3, 2), \\quad B=(4, \-1)$  
        \\item $A=(4, \-5), \\quad B=(-3, 4)$  
        \\item $A=(-2, 6), \\quad B=(5, 2)$  
        \\item $A=(1, \-4), \\quad B=(-2, 3)$  
    \\end{itemize}  
\\end{minipage}  
\\end{center}  
% \--- FIN\_SECCION: EJERCICIOS \---

\\newpage

% \--- INICIO\_SECCION: RESOLUCIONES \---  
\\section\*{\\centering Ejercicios Resueltos}

\\noindent  
\\begin{minipage}\[t\]{0.55\\textwidth}  
    $A=(-4, 7), \\quad B=(2, 3)$  
    \\begin{align\*}  
        \\dfrac{x \- (-4)}{(2) \- (-4)} &= \\dfrac{y \- (7)}{(3) \- (7)} \\\\  
        \\dfrac{x \+ 4}{2 \+ 4} &= \\dfrac{y \- 7}{-4} \\\\  
        \\dfrac{x \+ 4}{6} &= \\dfrac{y \- 7}{-4} \\\\  
        \-4(x \+ 4\) &= 6(y \- 7\) \\\\  
        \-4x \- 16 &= 6y \- 42 \\\\  
        \-4x \- 6y \+ 26 &= 0 \\\\  
        \\mathbf{-2x \- 3y \+ 13 \= 0}  
    \\end{align\*}  
    \\textbf{Comprobación:} \\\\  
    \\begin{minipage}\[t\]{0.45\\linewidth}  
        $A(-4, 7)$  
        \\begin{align\*}  
            \-2(-4) \- 3(7) \+ 13 &= 0 \\\\  
            8 \- 21 \+ 13 &= 0 \\\\  
            21 \- 21 &= 0 \\\\  
            0 &= 0  
        \\end{align\*}  
    \\end{minipage}  
    \\hfill  
    \\begin{minipage}\[t\]{0.45\\linewidth}  
        $B(2, 3)$  
        \\begin{align\*}  
            \-2(2) \- 3(3) \+ 13 &= 0 \\\\  
            \-4 \- 9 \+ 13 &= 0 \\\\  
            \-13 \+ 13 &= 0 \\\\  
            0 &= 0  
        \\end{align\*}  
    \\end{minipage}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.40\\textwidth}  
    \\centering  
    \\begin{tikzpicture}\[scale=0.5\]  
        \\draw\[very thin, gray\!30\] (-6,-1) grid (4,9);  
        \\draw\[-\>, ultra thick\] (-6,0) \-- (4,0) node\[right\] {$x$};  
        \\draw\[-\>, ultra thick\] (0,-1) \-- (0,9) node\[above\] {$y$};  
        \\draw\[domain=-5.5:3.5, smooth, variable=\\x, red, ultra thick\] plot ({\\x}, {-0.66\*\\x \+ 4.33});  
        \\fill\[black\] (-4,7) circle (4pt);  
        \\fill\[black\] (2,3) circle (4pt);  
    \\end{tikzpicture}  
\\end{minipage}

\\vspace{1.5em}  
\\hrule  
\\vspace{1.5em}

\\noindent  
\\begin{minipage}\[t\]{0.55\\textwidth}  
    $A=(3, \-2), \\quad B=(-2, \-3)$  
    \\begin{align\*}  
        \\dfrac{x \- (3)}{(-2) \- (3)} &= \\dfrac{y \- (-2)}{(-3) \- (-2)} \\\\  
        \\dfrac{x \- 3}{-5} &= \\dfrac{y \+ 2}{-1} \\\\  
        \-1(x \- 3\) &= \-5(y \+ 2\) \\\\  
        \-x \+ 3 &= \-5y \- 10 \\\\  
        \-x \+ 5y \+ 13 &= 0 \\\\  
        \\mathbf{x \- 5y \- 13 \= 0}  
    \\end{align\*}  
    \\textbf{Comprobación:} \\\\  
    \\begin{minipage}\[t\]{0.45\\linewidth}  
        $A(3, \-2)$  
        \\begin{align\*}  
            (3) \- 5(-2) \- 13 &= 0 \\\\  
            3 \+ 10 \- 13 &= 0 \\\\  
            13 \- 13 &= 0 \\\\  
            0 &= 0  
        \\end{align\*}  
    \\end{minipage}  
    \\hfill  
    \\begin{minipage}\[t\]{0.45\\linewidth}  
        $B(-2, \-3)$  
        \\begin{align\*}  
            (-2) \- 5(-3) \- 13 &= 0 \\\\  
            \-2 \+ 15 \- 13 &= 0 \\\\  
            15 \- 15 &= 0 \\\\  
            0 &= 0  
        \\end{align\*}  
    \\end{minipage}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.40\\textwidth}  
    \\centering  
    \\begin{tikzpicture}\[scale=0.5\]  
        \\draw\[very thin, gray\!30\] (-4,-5) grid (5,2);  
        \\draw\[-\>, ultra thick\] (-4,0) \-- (5,0) node\[right\] {$x$};  
        \\draw\[-\>, ultra thick\] (0,-5) \-- (0,2) node\[above\] {$y$};  
        \\draw\[domain=-3:4.5, smooth, variable=\\x, purple, ultra thick\] plot ({\\x}, {0.2\*\\x \- 2.6});  
        \\fill\[black\] (3,-2) circle (4pt);  
        \\fill\[black\] (-2,-3) circle (4pt);  
    \\end{tikzpicture}  
\\end{minipage}

\\newpage

\\noindent  
\\begin{minipage}\[t\]{0.55\\textwidth}  
    $A=(-3, 2), \\quad B=(4, \-1)$  
    \\begin{align\*}  
        \\dfrac{x \- (-3)}{(4) \- (-3)} &= \\dfrac{y \- (2)}{(-1) \- (2)} \\\\  
        \\dfrac{x \+ 3}{7} &= \\dfrac{y \- 2}{-3} \\\\  
        \-3(x \+ 3\) &= 7(y \- 2\) \\\\  
        \-3x \- 9 &= 7y \- 14 \\\\  
        \-3x \- 7y \+ 5 &= 0 \\\\  
        \\mathbf{3x \+ 7y \- 5 \= 0}  
    \\end{align\*}  
    \\textbf{Comprobación:} \\\\  
    \\begin{minipage}\[t\]{0.45\\linewidth}  
        $A(-3, 2)$  
        \\begin{align\*}  
            3(-3) \+ 7(2) \- 5 &= 0 \\\\  
            \-9 \+ 14 \- 5 &= 0 \\\\  
            14 \- 14 &= 0 \\\\  
            0 &= 0  
        \\end{align\*}  
    \\end{minipage}  
    \\hfill  
    \\begin{minipage}\[t\]{0.45\\linewidth}  
        $B(4, \-1)$  
        \\begin{align\*}  
            3(4) \+ 7(-1) \- 5 &= 0 \\\\  
            12 \- 7 \- 5 &= 0 \\\\  
            12 \- 12 &= 0 \\\\  
            0 &= 0  
        \\end{align\*}  
    \\end{minipage}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.40\\textwidth}  
    \\centering  
    \\begin{tikzpicture}\[scale=0.5\]  
        \\draw\[very thin, gray\!30\] (-5,-3) grid (6,4);  
        \\draw\[-\>, ultra thick\] (-5,0) \-- (6,0) node\[right\] {$x$};  
        \\draw\[-\>, ultra thick\] (0,-3) \-- (0,4) node\[above\] {$y$};  
        \\draw\[domain=-4:5, smooth, variable=\\x, blue, ultra thick\] plot ({\\x}, {-0.428\*\\x \+ 0.714});  
        \\fill\[black\] (-3,2) circle (4pt);  
        \\fill\[black\] (4,-1) circle (4pt);  
    \\end{tikzpicture}  
\\end{minipage}

\\vspace{1.5em}  
\\hrule  
\\vspace{1.5em}

\\noindent  
\\begin{minipage}\[t\]{0.55\\textwidth}  
    $A=(4, \-5), \\quad B=(-3, 4)$  
    \\begin{align\*}  
        \\dfrac{x \- (4)}{(-3) \- (4)} &= \\dfrac{y \- (-5)}{(4) \- (-5)} \\\\  
        \\dfrac{x \- 4}{-7} &= \\dfrac{y \+ 5}{9} \\\\  
        9(x \- 4\) &= \-7(y \+ 5\) \\\\  
        9x \- 36 &= \-7y \- 35 \\\\  
        \\mathbf{9x \+ 7y \- 1 \= 0}  
    \\end{align\*}  
    \\textbf{Comprobación:} \\\\  
    \\begin{minipage}\[t\]{0.45\\linewidth}  
        $A(4, \-5)$  
        \\begin{align\*}  
            9(4) \+ 7(-5) \- 1 &= 0 \\\\  
            36 \- 35 \- 1 &= 0 \\\\  
            0 &= 0  
        \\end{align\*}  
    \\end{minipage}  
    \\hfill  
    \\begin{minipage}\[t\]{0.45\\linewidth}  
        $B(-3, 4)$  
        \\begin{align\*}  
            9(-3) \+ 7(4) \- 1 &= 0 \\\\  
            \-27 \+ 28 \- 1 &= 0 \\\\  
            0 &= 0  
        \\end{align\*}  
    \\end{minipage}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.40\\textwidth}  
    \\centering  
    \\begin{tikzpicture}\[scale=0.5\]  
        \\draw\[very thin, gray\!30\] (-5,-6) grid (6,6);  
        \\draw\[-\>, ultra thick\] (-5,0) \-- (6,0) node\[right\] {$x$};  
        \\draw\[-\>, ultra thick\] (0,-6) \-- (0,6) node\[above\] {$y$};  
        \\draw\[domain=-4:4.5, smooth, variable=\\x, green\!50\!black, ultra thick\] plot ({\\x}, {-1.28\*\\x \+ 0.14});  
        \\fill\[black\] (4,-5) circle (4pt);  
        \\fill\[black\] (-3,4) circle (4pt);  
    \\end{tikzpicture}  
\\end{minipage}

\\newpage

\\noindent  
\\begin{minipage}\[t\]{0.55\\textwidth}  
    $A=(-2, 6), \\quad B=(5, 2)$  
    \\begin{align\*}  
        \\dfrac{x \- (-2)}{(5) \- (-2)} &= \\dfrac{y \- (6)}{(2) \- (6)} \\\\  
        \\dfrac{x \+ 2}{7} &= \\dfrac{y \- 6}{-4} \\\\  
        \-4(x \+ 2\) &= 7(y \- 6\) \\\\  
        \-4x \- 8 &= 7y \- 42 \\\\  
        \-4x \- 7y \+ 34 &= 0 \\\\  
        \\mathbf{4x \+ 7y \- 34 \= 0}  
    \\end{align\*}  
    \\textbf{Comprobación:} \\\\  
    \\begin{minipage}\[t\]{0.45\\linewidth}  
        $A(-2, 6)$  
        \\begin{align\*}  
            4(-2) \+ 7(6) \- 34 &= 0 \\\\  
            \-8 \+ 42 \- 34 &= 0 \\\\  
            42 \- 42 &= 0 \\\\  
            0 &= 0  
        \\end{align\*}  
    \\end{minipage}  
    \\hfill  
    \\begin{minipage}\[t\]{0.45\\linewidth}  
        $B(5, 2)$  
        \\begin{align\*}  
            4(5) \+ 7(2) \- 34 &= 0 \\\\  
            20 \+ 14 \- 34 &= 0 \\\\  
            34 \- 34 &= 0 \\\\  
            0 &= 0  
        \\end{align\*}  
    \\end{minipage}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.40\\textwidth}  
    \\centering  
    \\begin{tikzpicture}\[scale=0.5\]  
        \\draw\[very thin, gray\!30\] (-4,-1) grid (7,8);  
        \\draw\[-\>, ultra thick\] (-4,0) \-- (7,0) node\[right\] {$x$};  
        \\draw\[-\>, ultra thick\] (0,-1) \-- (0,8) node\[above\] {$y$};  
        \\draw\[domain=-3:6.5, smooth, variable=\\x, orange, ultra thick\] plot ({\\x}, {-0.57\*\\x \+ 4.85});  
        \\fill\[black\] (-2,6) circle (4pt);  
        \\fill\[black\] (5,2) circle (4pt);  
    \\end{tikzpicture}  
\\end{minipage}

\\vspace{1.5em}  
\\hrule  
\\vspace{1.5em}

\\noindent  
\\begin{minipage}\[t\]{0.55\\textwidth}  
    $A=(1, \-4), \\quad B=(-2, 3)$  
    \\begin{align\*}  
        \\dfrac{x \- (1)}{(-2) \- (1)} &= \\dfrac{y \- (-4)}{(3) \- (-4)} \\\\  
        \\dfrac{x \- 1}{-3} &= \\dfrac{y \+ 4}{7} \\\\  
        7(x \- 1\) &= \-3(y \+ 4\) \\\\  
        7x \- 7 &= \-3y \- 12 \\\\  
        7x \+ 3y \+ 5 &= 0 \\\\  
        \\mathbf{7x \+ 3y \+ 5 \= 0}  
    \\end{align\*}  
    \\textbf{Comprobación:} \\\\  
    \\begin{minipage}\[t\]{0.45\\linewidth}  
        $A(1, \-4)$  
        \\begin{align\*}  
            7(1) \+ 3(-4) \+ 5 &= 0 \\\\  
            7 \- 12 \+ 5 &= 0 \\\\  
            12 \- 12 &= 0 \\\\  
            0 &= 0  
        \\end{align\*}  
    \\end{minipage}  
    \\hfill  
    \\begin{minipage}\[t\]{0.45\\linewidth}  
        $B(-2, 3)$  
        \\begin{align\*}  
            7(-2) \+ 3(3) \+ 5 &= 0 \\\\  
            \-14 \+ 9 \+ 5 &= 0 \\\\  
            \-14 \+ 14 &= 0 \\\\  
            0 &= 0  
        \\end{align\*}  
    \\end{minipage}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.40\\textwidth}  
    \\centering  
    \\begin{tikzpicture}\[scale=0.5\]  
        \\draw\[very thin, gray\!30\] (-4,-6) grid (4,6);  
        \\draw\[-\>, ultra thick\] (-4,0) \-- (4,0) node\[right\] {$x$};  
        \\draw\[-\>, ultra thick\] (0,-6) \-- (0,6) node\[above\] {$y$};  
        \\draw\[domain=-3:1.5, smooth, variable=\\x, cyan, ultra thick\] plot ({\\x}, {-2.33\*\\x \- 1.66});  
        \\fill\[black\] (1,-4) circle (4pt);  
        \\fill\[black\] (-2,3) circle (4pt);  
    \\end{tikzpicture}  
\\end{minipage}  
% \--- FIN\_SECCION: RESOLUCIONES \---

\\newpage

% \--- INICIO\_SECCION: EXTRAS \---  
\\section\*{\\centering Ejercicios Extras}

\\noindent  
\\begin{minipage}\[t\]{0.48\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 1}\\end{center}  
    \\begin{itemize}  
        \\item $A=(1, 1), \\quad B=(3, 5)$  
        \\item $A=(-2, 4), \\quad B=(1, \-2)$  
        \\item $A=(0, 0), \\quad B=(-4, 2)$  
        \\item $A=(-5, \-5), \\quad B=(5, 5)$  
        \\item $A=(2, 6), \\quad B=(-3, 1)$  
        \\item $A=(4, 0), \\quad B=(0, \-8)$  
    \\end{itemize}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.48\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 2}\\end{center}  
    \\begin{itemize}  
        \\item $A=(3, 3), \\quad B=(-3, \-3)$  
        \\item $A=(-1, 7), \\quad B=(2, 4)$  
        \\item $A=(6, \-2), \\quad B=(-2, 6)$  
        \\item $A=(0, 5), \\quad B=(5, 0)$  
        \\item $A=(-4, \-2), \\quad B=(4, 2)$  
        \\item $A=(3, \-1), \\quad B=(1, 3)$  
    \\end{itemize}  
\\end{minipage}  
% \--- FIN\_SECCION: EXTRAS \---

\\end{document}

# 8 pendiente ordenada al origen

este tema repetimos el mismo tema pendiente ordenada al origen, de matematicas 1\. duplicamos el html para ponerlo aqui

# 9 REsolucion de triángulos, teorema de pitagoras

\\documentclass\[11pt, a4paper\]{article}

% \--- UNIVERSAL PREAMBLE BLOCK \---  
\\usepackage\[a4paper, top=2cm, bottom=2cm, left=1.5cm, right=1.5cm\]{geometry}  
\\usepackage{fontspec}  
\\usepackage\[spanish, bidi=basic, provide=\*\]{babel}

\\babelprovide\[import, onchar=ids fonts\]{spanish}  
\\babelprovide\[import, onchar=ids fonts\]{english}

% Set default font to Sans Serif in the main (rm) slot  
\\babelfont{rm}{Noto Sans}

\\usepackage{amsmath, amssymb}  
\\usepackage{enumitem}  
\\usepackage{tikz}

% Eliminar numeración de páginas  
\\pagestyle{empty}

% Configuración para listas sin numeración ni viñetas  
\\setlist\[itemize\]{label={}, leftmargin=0pt, itemsep=1.5em}

\\begin{document}

% Título principal centrado con línea separadora  
\\begin{center}  
    \\Huge \\textbf{Teorema de Pitágoras} \\\\  
    \\vspace{0.5em}  
    \\hrule  
\\end{center}

\\vspace{1em}

% \--- INICIO\_SECCION: MINI\_APUNTE \---  
\\section\*{\\centering Mini Apunte}

En todo triángulo rectángulo, el cuadrado de la hipotenusa es igual a la suma de los cuadrados de los catetos. Esta relación nos permite encontrar un lado desconocido si conocemos los otros dos.

\\vspace{1em}  
\\begin{center}  
    \\begin{tikzpicture}\[scale=0.8\]  
        \\draw\[thick\] (0,0) \-- (3,0) node\[midway, below\] {$b$} \-- (0,4) node\[midway, above right\] {$c$} \-- cycle node\[midway, left\] {$a$};  
        \\draw (0,0) rectangle (0.3,0.3);  
    \\end{tikzpicture}  
    \\quad  
    \\begin{minipage}{0.5\\textwidth}  
        \\begin{itemize}  
            \\item \\textbf{Teorema de Pitágoras:}  
            \\item $c^2 \= a^2 \+ b^2$  
            \\item $c \= \\sqrt{a^2 \+ b^2} \\quad a \= \\sqrt{c^2 \- b^2} \\quad b \= \\sqrt{c^2 \- a^2}$  
            \\item \\textbf{Razones Trigonométricas:}  
            \\item $\\sin \\theta \= \\frac{Co}{hip} \\quad \\cos \\theta \= \\frac{Ca}{hip} \\quad \\tan \\theta \= \\frac{Co}{Ca}$  
            \\item Estas razones las utilizaremos para encontrar el valor del ángulo.  
        \\end{itemize}  
    \\end{minipage}  
\\end{center}  
% \--- FIN\_SECCION: MINI\_APUNTE \---

\\vspace{1em}  
\\hrule  
\\vspace{1em}

% \--- INICIO\_SECCION: EJEMPLOS \---  
\\section\*{\\centering Ejemplo}

\\noindent  
\\begin{minipage}\[t\]{0.4\\textwidth}  
    \\centering  
    \\begin{tikzpicture}\[scale=1.2\]  
        \\draw\[thick\] (0,0) \-- (2,0) node\[midway, below\] {$z$} \-- (0,1.5) node\[midway, left\] {$10$} \-- cycle node\[midway, above right\] {$15$};  
        \\draw (0,0) rectangle (0.2,0.2);  
        \\node at (0.3,1.1) {$\\alpha$};  
        \\node at (1.5,0.2) {$\\beta$};  
    \\end{tikzpicture}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.55\\textwidth}  
    \\begin{itemize}  
        \\item \\textbf{Cálculo del lado $z$:}  
        \\begin{align\*}  
            z &= \\sqrt{(15)^2 \- (10)^2} \\\\  
            z &= \\sqrt{225 \- 100} \\\\  
            z &= \\sqrt{125} \\\\  
            \\mathbf{z} &\\mathbf{\\approx 11.18}  
        \\end{align\*}  
        \\item \\textbf{Cálculo del ángulo $\\alpha$:}  
        \\begin{align\*}  
            \\cos \\alpha &= \\frac{Ca}{hip} \= \\frac{10}{15} \\\\  
            \\cos \\alpha &= 0.66   
        \\end{align\*}  
        \\small \\textit{Buscar en tablas o en la calculadora a qué ángulo $\\alpha$ corresponde el $\\cos \\alpha \= 0.66$.}  
        \\begin{align\*}  
            \\mathbf{\\alpha} &\\mathbf{= 48^\\circ}  
        \\end{align\*}  
        \\item \\textbf{Cálculo del ángulo $\\beta$:}  
        \\begin{align\*}  
            90 \+ 48 \+ \\beta &= 180 \\\\  
            \\beta &= 180 \- 90 \- 48 \\\\  
            \\mathbf{\\beta} &\\mathbf{= 42^\\circ}  
        \\end{align\*}  
    \\end{itemize}  
\\end{minipage}  
% \--- FIN\_SECCION: EJEMPLOS \---

\\vspace{2em}  
\\hrule  
\\vspace{1em}

% \--- INICIO\_SECCION: EJERCICIOS \---  
\\section\*{\\centering Ejercicios}

\\begin{center}  
\\begin{tikzpicture}\[scale=0.6\]  
    % Triángulo 1  
    \\begin{scope}\[shift={(0,0)}\]  
        \\draw\[thick\] (0,0) \-- (2,0) node\[midway, below\] {$x$} \-- (0,3) node\[midway, left\] {$8$} \-- cycle node\[midway, above right\] {$16$};  
        \\node at (0.3,2.4) {$\\alpha$}; \\node at (1.5,0.3) {$\\beta$};  
    \\end{scope}  
    % Triángulo 2  
    \\begin{scope}\[shift={(6,0)}\]  
        \\draw\[thick\] (0,0) \-- (3,0) node\[midway, below\] {$8$} \-- (0,1.5) node\[midway, left\] {$4$} \-- cycle node\[midway, above right\] {$y$};  
        \\node at (0.3,0.9) {$\\alpha$}; \\node at (2.4,0.3) {$\\beta$};  
    \\end{scope}  
    % Triángulo 3  
    \\begin{scope}\[shift={(12,0)}\]  
        \\draw\[thick\] (0,0) \-- (1.5,0) node\[midway, below\] {$5$} \-- (0,2.5) node\[midway, left\] {$a$} \-- cycle node\[midway, above right\] {$9$};  
        \\node at (0.3,2) {$\\alpha$}; \\node at (1,0.3) {$\\beta$};  
    \\end{scope}  
\\end{tikzpicture}  
\\end{center}

\\vspace{2em}

\\begin{center}  
\\begin{tikzpicture}\[scale=0.6\]  
    % Triángulo 4  
    \\begin{scope}\[shift={(0,0)}\]  
        \\draw\[thick\] (0,0) \-- (1,0) node\[midway, below\] {$4$} \-- (0,3) node\[midway, left\] {$12$} \-- cycle node\[midway, above right\] {$y$};  
        \\node at (0.3,2.5) {$\\alpha$}; \\node at (0.7,0.3) {$\\beta$};  
    \\end{scope}  
    % Triángulo 5  
    \\begin{scope}\[shift={(6,0)}\]  
        \\draw\[thick\] (0,0) \-- (3,0) node\[midway, below\] {$x$} \-- (0,1.5) node\[midway, left\] {$9$} \-- cycle node\[midway, above right\] {$20$};  
        \\node at (0.3,0.9) {$\\alpha$}; \\node at (2.4,0.3) {$\\beta$};  
    \\end{scope}  
    % Triángulo 6  
    \\begin{scope}\[shift={(12,0)}\]  
        \\draw\[thick\] (0,0) \-- (2,0) node\[midway, below\] {$6$} \-- (0,2) node\[midway, left\] {$y$} \-- cycle node\[midway, above right\] {$9$};  
        \\node at (0.3,1.5) {$\\alpha$}; \\node at (1.5,0.3) {$\\beta$};  
    \\end{scope}  
\\end{tikzpicture}  
\\end{center}  
% \--- FIN\_SECCION: EJERCICIOS \---

\\newpage

% \--- INICIO\_SECCION: RESOLUCIONES \---  
\\section\*{\\centering Ejercicios Resueltos}

\\begin{itemize}  
    \\item \\textbf{Ejercicio 1}  
    \\begin{align\*}  
        x &= \\sqrt{16^2 \- 8^2} \\\\  
        x &= \\sqrt{256 \- 64} \\\\  
        x &= \\sqrt{192} \\\\  
        \\mathbf{x} &\\mathbf{\\approx 13.86} \\\\  
        \\cos \\alpha &= \\frac{8}{16} \\\\  
        \\cos \\alpha &= 0.5 \\\\  
        \\mathbf{\\alpha} &\\mathbf{= 60^\\circ} \\\\  
        \\beta &= 180 \- 90 \- 60 \\\\  
        \\mathbf{\\beta} &\\mathbf{= 30^\\circ}  
    \\end{align\*}  
    \\hrule  
    \\item \\textbf{Ejercicio 2}  
    \\begin{align\*}  
        y &= \\sqrt{4^2 \+ 8^2} \\\\  
        y &= \\sqrt{16 \+ 64} \\\\  
        y &= \\sqrt{80} \\\\  
        \\mathbf{y} &\\mathbf{\\approx 8.94} \\\\  
        \\cos \\alpha &= \\frac{4}{8.94} \\\\  
        \\cos \\alpha &= 0.447 \\\\  
        \\mathbf{\\alpha} &\\mathbf{\\approx 63.43^\\circ} \\\\  
        \\beta &= 180 \- 90 \- 63.43 \\\\  
        \\mathbf{\\beta} &\\mathbf{\\approx 26.57^\\circ}  
    \\end{align\*}  
    \\hrule  
    \\item \\textbf{Ejercicio 3}  
    \\begin{align\*}  
        a &= \\sqrt{9^2 \- 5^2} \\\\  
        a &= \\sqrt{81 \- 25} \\\\  
        a &= \\sqrt{56} \\\\  
        \\mathbf{a} &\\mathbf{\\approx 7.48} \\\\  
        \\cos \\alpha &= \\frac{7.48}{9} \\\\  
        \\cos \\alpha &= 0.831 \\\\  
        \\mathbf{\\alpha} &\\mathbf{\\approx 33.79^\\circ} \\\\  
        \\beta &= 180 \- 90 \- 33.79 \\\\  
        \\mathbf{\\beta} &\\mathbf{\\approx 56.21^\\circ}  
    \\end{align\*}  
    \\hrule  
    \\item \\textbf{Ejercicio 4}  
    \\begin{align\*}  
        y &= \\sqrt{12^2 \+ 4^2} \\\\  
        y &= \\sqrt{144 \+ 16} \\\\  
        y &= \\sqrt{160} \\\\  
        \\mathbf{y} &\\mathbf{\\approx 12.65} \\\\  
        \\cos \\alpha &= \\frac{12}{12.65} \\\\  
        \\cos \\alpha &= 0.948 \\\\  
        \\mathbf{\\alpha} &\\mathbf{\\approx 18.43^\\circ} \\\\  
        \\beta &= 180 \- 90 \- 18.43 \\\\  
        \\mathbf{\\beta} &\\mathbf{\\approx 71.57^\\circ}  
    \\end{align\*}  
    \\hrule  
    \\item \\textbf{Ejercicio 5}  
    \\begin{align\*}  
        x &= \\sqrt{20^2 \- 9^2} \\\\  
        x &= \\sqrt{400 \- 81} \\\\  
        x &= \\sqrt{319} \\\\  
        \\mathbf{x} &\\mathbf{\\approx 17.86} \\\\  
        \\cos \\alpha &= \\frac{9}{20} \\\\  
        \\cos \\alpha &= 0.45 \\\\  
        \\mathbf{\\alpha} &\\mathbf{\\approx 63.26^\\circ} \\\\  
        \\beta &= 180 \- 90 \- 63.26 \\\\  
        \\mathbf{\\beta} &\\mathbf{\\approx 26.74^\\circ}  
    \\end{align\*}  
    \\hrule  
    \\item \\textbf{Ejercicio 6}  
    \\begin{align\*}  
        y &= \\sqrt{9^2 \- 6^2} \\\\  
        y &= \\sqrt{81 \- 36} \\\\  
        y &= \\sqrt{45} \\\\  
        \\mathbf{y} &\\mathbf{\\approx 6.71} \\\\  
        \\cos \\beta &= \\frac{6}{9} \\\\  
        \\cos \\beta &= 0.666 \\\\  
        \\mathbf{\\beta} &\\mathbf{\\approx 48.19^\\circ} \\\\  
        \\alpha &= 180 \- 90 \- 48.19 \\\\  
        \\mathbf{\\alpha} &\\mathbf{\\approx 41.81^\\circ}  
    \\end{align\*}  
\\end{itemize}  
% \--- FIN\_SECCION: RESOLUCIONES \---

\\newpage

% \--- INICIO\_SECCION: EXTRAS \---  
\\section\*{\\centering Ejercicios Extras}

\\begin{center}\\textbf{\\large Bloque 1}\\end{center}  
\\begin{center}  
\\begin{tikzpicture}\[scale=0.5\]  
    % Fila 1  
    \\begin{scope}\[shift={(0,0)}\]  
        \\draw\[thick\] (0,0) \-- (3,0) node\[midway, below\] {$x$} \-- (0,1.2) node\[midway, left\] {$7$} \-- cycle node\[midway, above right\] {$25$};  
        \\node at (0.4,0.7) {$\\alpha$};  
    \\end{scope}  
    \\begin{scope}\[shift={(6,0)}\]  
        \\draw\[thick\] (0,0) \-- (2.5,0) node\[midway, below\] {$12$} \-- (0,1) node\[midway, left\] {$5$} \-- cycle node\[midway, above right\] {$y$};  
        \\node at (1.8,0.3) {$\\beta$};  
    \\end{scope}  
    \\begin{scope}\[shift={(12,0)}\]  
        \\draw\[thick\] (0,0) \-- (2.2,0) node\[midway, below\] {$12$} \-- (0,1.5) node\[midway, left\] {$a$} \-- cycle node\[midway, above right\] {$13$};  
    \\end{scope}  
    % Fila 2  
    \\begin{scope}\[shift={(0,-4)}\]  
        \\draw\[thick\] (0,0) \-- (1.5,0) node\[midway, below\] {$x$} \-- (0,2.5) node\[midway, left\] {$15$} \-- cycle node\[midway, above right\] {$17$};  
    \\end{scope}  
    \\begin{scope}\[shift={(6,-4)}\]  
        \\draw\[thick\] (0,0) \-- (2.5,0) node\[midway, below\] {$21$} \-- (0,2.2) node\[midway, left\] {$20$} \-- cycle node\[midway, above right\] {$h$};  
    \\end{scope}  
    \\begin{scope}\[shift={(12,-4)}\]  
        \\draw\[thick\] (0,0) \-- (2.2,0) node\[midway, below\] {$8$} \-- (0,1.8) node\[midway, left\] {$Ca$} \-- cycle node\[midway, above right\] {$10$};  
        \\node at (0.4,1.2) {$\\alpha$};  
    \\end{scope}  
\\end{tikzpicture}  
\\end{center}

\\vspace{2em}

\\begin{center}\\textbf{\\large Bloque 2}\\end{center}  
\\begin{center}  
\\begin{tikzpicture}\[scale=0.5\]  
    % Fila 1  
    \\begin{scope}\[shift={(0,0)}\]  
        \\draw\[thick\] (0,0) \-- (2,0) node\[midway, below\] {$z$} \-- (0,1.2) node\[midway, left\] {$9$} \-- cycle node\[midway, above right\] {$15$};  
    \\end{scope}  
    \\begin{scope}\[shift={(6,0)}\]  
        \\draw\[thick\] (0,0) \-- (2,0) node\[midway, below\] {$Co$} \-- (0,1.5) node\[midway, left\] {$6$} \-- cycle node\[midway, above right\] {$12$};  
        \\node at (1.5,0.3) {$\\beta$};  
    \\end{scope}  
    \\begin{scope}\[shift={(12,0)}\]  
        \\draw\[thick\] (0,0) \-- (1.5,0) node\[midway, below\] {$1$} \-- (0,1.5) node\[midway, left\] {$1$} \-- cycle node\[midway, above right\] {$x$};  
    \\end{scope}  
    % Fila 2  
    \\begin{scope}\[shift={(0,-4)}\]  
        \\draw\[thick\] (0,0) \-- (2.2,0) node\[midway, below\] {$y$} \-- (0,1.5) node\[midway, left\] {$6$} \-- cycle node\[midway, above right\] {$10$};  
    \\end{scope}  
    \\begin{scope}\[shift={(6,-4)}\]  
        \\draw\[thick\] (0,0) \-- (3,0) node\[midway, below\] {$60$} \-- (0,1) node\[midway, left\] {$11$} \-- cycle node\[midway, above right\] {$hip$};  
    \\end{scope}  
    \\begin{scope}\[shift={(12,-4)}\]  
        \\draw\[thick\] (0,0) \-- (1.5,0) node\[midway, below\] {$5$} \-- (0,2.5) node\[midway, left\] {$Ca$} \-- cycle node\[midway, above right\] {$13$};  
        \\node at (0.4,1.8) {$\\alpha$};  
    \\end{scope}  
\\end{tikzpicture}  
\\end{center}  
% \--- FIN\_SECCION: EXTRAS \---

\\end{document}

# 10 razones trigonométricas

\\documentclass\[11pt\]{article}  
\\usepackage\[margin=1.5cm\]{geometry}  
\\usepackage{fontspec}  
\\setmainfont{Noto Sans}  
\\usepackage{amsmath, amssymb}  
\\usepackage{enumitem}  
\\usepackage{tikz}  
\\pagestyle{empty}

\\begin{document}

% \--- INICIO\_SECCION: TITULO \---  
\\begin{center}  
    {\\Huge \\textbf{Resolución de Triángulos Rectángulos}} \\\\  
    \\vspace{0.5em}  
    \\hrule  
\\end{center}  
% \--- FIN\_SECCION: TITULO \---

\\vspace{1em}

% \--- INICIO\_SECCION: MINI\_APUNTE \---  
\\section\*{\\centering Razones Trigonométricas}

\\noindent  
\\begin{minipage}\[t\]{0.5\\textwidth}  
    \\centering  
    \\begin{tikzpicture}\[scale=1.2\]  
        \\draw\[thick\] (0,0) \-- (3,0) node\[midway, below\] {$b$} \-- (0,2) node\[midway, right\] {$c$} \-- cycle node\[midway, left\] {$a$};  
        \\draw (2.5,0) arc (180:146:0.5);  
        \\node at (2.3,0.2) {$\\alpha$};  
        \\draw (0,1.5) arc (270:303:0.5);  
        \\node at (0.2,1.3) {$\\beta$};  
        \\draw (0,0) rectangle (0.2,0.2);  
    \\end{tikzpicture}  
\\end{minipage}  
\\begin{minipage}\[t\]{0.5\\textwidth}  
    \\begin{itemize}\[label={}, leftmargin=0pt\]  
        \\item $Sen \= \\frac{co}{hip}$ \\hspace{1em} $co$: cateto opuesto  
        \\item $Cos \= \\frac{ca}{hip}$ \\hspace{1em} $ca$: cateto adyacente  
        \\item $Tan \= \\frac{co}{ca}$ \\hspace{1em} $hip$: hipotenusa  
    \\end{itemize}  
\\end{minipage}

\\vspace{1em}  
\\hrule  
\\vspace{1em}

% \--- INICIO\_SECCION: EJEMPLOS \---  
\\section\*{\\centering Ejemplo}

\\noindent  
\\begin{minipage}\[t\]{0.4\\textwidth}  
    \\centering  
    \\begin{tikzpicture}\[scale=1.5\]  
        \\draw\[thick\] (0,0) \-- (2,0) node\[midway, below\] {$y$} \-- (0,2.5) node\[midway, right\] {$12$} \-- cycle node\[midway, left\] {$x$};  
        \\draw (1.5,0) arc (180:129:0.5);  
        \\node at (1.2,0.25) {$35^\\circ$};  
        \\draw (0,2) arc (270:308:0.5);  
        \\node at (0.2,1.8) {$\\beta$};  
        \\draw (0,0) rectangle (0.2,0.2);  
    \\end{tikzpicture}  
\\end{minipage}  
\\begin{minipage}\[t\]{0.6\\textwidth}  
    ¿Qué lado conoces con respecto al ángulo de $35^\\circ$?  
    R. La hipotenusa.  
      
    ¿Qué funciones trigonométricas podrías usar?  
    R. Seno y coseno.

    \\begin{align\*}  
        Sen\\,35^\\circ &= \\frac{x}{12} \\\\  
        12 \\cdot Sen\\,35^\\circ &= x \\\\  
        12 \\cdot (0.57) &= x \\\\  
        \\mathbf{x} &= \\mathbf{6.84}  
    \\end{align\*}  
\\end{minipage}

\\vspace{1em}

\\noindent  
\\begin{minipage}\[t\]{0.5\\textwidth}  
    \\begin{align\*}  
        Cos\\,35^\\circ &= \\frac{y}{12} \\\\  
        12 \\cdot Cos\\,35^\\circ &= y \\\\  
        12 \\cdot (0.81) &= y \\\\  
        \\mathbf{y} &= \\mathbf{9.72}  
    \\end{align\*}  
\\end{minipage}  
\\begin{minipage}\[t\]{0.5\\textwidth}  
    Encuentra $\\beta$:  
    \\begin{align\*}  
        90 \+ 35 \+ \\beta &= 180 \\\\  
        \\beta &= 180 \- 90 \- 35 \\\\  
        \\mathbf{\\beta} &= \\mathbf{55^\\circ}  
    \\end{align\*}  
\\end{minipage}  
% \--- FIN\_SECCION: EJEMPLOS \---

\\vspace{1em}  
\\hrule  
\\vspace{1em}

% \--- INICIO\_SECCION: EJERCICIOS \---  
\\section\*{\\centering Ejercicios}

\\noindent  
\\begin{minipage}\[t\]{0.5\\textwidth}  
    \\centering  
    \\begin{tikzpicture}\[scale=1.1\]  
        \\draw\[thick\] (0,0) \-- (2,0) node\[midway, below\] {$y$} \-- (0,2.5) node\[midway, right\] {$16$} \-- cycle node\[midway, left\] {$x$};  
        \\draw (1.5,0) arc (180:129:0.5);  
        \\node at (1.2,0.25) {$42^\\circ$};  
        \\draw (0,2) arc (270:308:0.5);  
        \\node at (0.2,1.8) {$\\beta$};  
        \\draw (0,0) rectangle (0.2,0.2);  
    \\end{tikzpicture}  
\\end{minipage}  
\\begin{minipage}\[t\]{0.5\\textwidth}  
    \\centering  
    \\begin{tikzpicture}\[scale=1.1\]  
        \\draw\[thick\] (0,0) \-- (2.5,0) node\[midway, below\] {$b$} \-- (0,2) node\[midway, right\] {$10$} \-- cycle node\[midway, left\] {$a$};  
        \\draw (2,0) arc (180:141:0.5);  
        \\node at (1.7,0.25) {$36^\\circ$};  
        \\draw (0,1.5) arc (270:321:0.5);  
        \\node at (0.2,1.3) {$\\beta$};  
        \\draw (0,0) rectangle (0.2,0.2);  
    \\end{tikzpicture}  
\\end{minipage}

\\vspace{2em}

\\noindent  
\\begin{minipage}\[t\]{0.5\\textwidth}  
    \\centering  
    \\begin{tikzpicture}\[scale=1.1\]  
        \\draw\[thick\] (0,0) \-- (3,0) node\[midway, below\] {$y$} \-- (0,2.5) node\[midway, right\] {$12$} \-- cycle node\[midway, left\] {$x$};  
        \\draw (2.5,0) arc (180:140:0.5);  
        \\node at (2.2,0.25) {$\\alpha$};  
        \\draw (0,2) arc (270:320:0.5);  
        \\node at (0.2,1.7) {$30^\\circ$};  
        \\draw (0,0) rectangle (0.2,0.2);  
    \\end{tikzpicture}  
\\end{minipage}  
\\begin{minipage}\[t\]{0.5\\textwidth}  
    \\centering  
    \\begin{tikzpicture}\[scale=1.1\]  
        \\draw\[thick\] (0,0) \-- (3.5,0) node\[midway, below\] {$b$} \-- (0,1.5) node\[midway, right\] {$z$} \-- cycle node\[midway, left\] {$10$};  
        \\draw (3,0) arc (180:157:0.5);  
        \\node at (2.7,0.2) {$\\alpha$};  
        \\draw (0,1) arc (270:336:0.5);  
        \\node at (0.3,0.8) {$14^\\circ$};  
        \\draw (0,0) rectangle (0.2,0.2);  
    \\end{tikzpicture}  
\\end{minipage}  
% \--- FIN\_SECCION: EJERCICIOS \---

\\newpage

% \--- INICIO\_SECCION: RESOLUCIONES \---  
\\section\*{\\centering Resoluciones}

\\noindent  
\\begin{minipage}\[t\]{0.35\\textwidth}  
    \\centering  
    \\begin{tikzpicture}\[scale=0.8\]  
        \\draw\[thick\] (0,0) \-- (2,0) node\[midway, below\] {$y$} \-- (0,2.5) node\[midway, right\] {$16$} \-- cycle node\[midway, left\] {$x$};  
        \\node at (1.2,0.25) {$42^\\circ$};  
        \\draw (0,0) rectangle (0.15,0.15);  
    \\end{tikzpicture}  
\\end{minipage}  
\\begin{minipage}\[t\]{0.65\\textwidth}  
    \\begin{align\*}  
        Sen\\,42^\\circ &= \\frac{y}{16} \\\\  
        16 \\cdot (0.669) &= y \\\\  
        \\mathbf{y} &= \\mathbf{10.7} \\\\  
        Cos\\,42^\\circ &= \\frac{x}{16} \\\\  
        16 \\cdot (0.743) &= x \\\\  
        \\mathbf{x} &= \\mathbf{11.89} \\\\  
        \\beta &= 180 \- 90 \- 42 \\\\  
        \\mathbf{\\beta} &= \\mathbf{48^\\circ}  
    \\end{align\*}  
\\end{minipage}

\\vspace{1em}  
\\hrule  
\\vspace{1em}

\\noindent  
\\begin{minipage}\[t\]{0.35\\textwidth}  
    \\centering  
    \\begin{tikzpicture}\[scale=0.8\]  
        \\draw\[thick\] (0,0) \-- (2.5,0) node\[midway, below\] {$b$} \-- (0,2) node\[midway, right\] {$10$} \-- cycle node\[midway, left\] {$a$};  
        \\node at (1.7,0.25) {$36^\\circ$};  
        \\draw (0,0) rectangle (0.15,0.15);  
    \\end{tikzpicture}  
\\end{minipage}  
\\begin{minipage}\[t\]{0.65\\textwidth}  
    \\begin{align\*}  
        Sen\\,36^\\circ &= \\frac{a}{10} \\\\  
        10 \\cdot (0.587) &= a \\\\  
        \\mathbf{a} &= \\mathbf{5.87} \\\\  
        Cos\\,36^\\circ &= \\frac{b}{10} \\\\  
        10 \\cdot (0.809) &= b \\\\  
        \\mathbf{b} &= \\mathbf{8.09} \\\\  
        \\beta &= 180 \- 90 \- 36 \\\\  
        \\mathbf{\\beta} &= \\mathbf{54^\\circ}  
    \\end{align\*}  
\\end{minipage}

\\vspace{1em}  
\\hrule  
\\vspace{1em}

\\noindent  
\\begin{minipage}\[t\]{0.35\\textwidth}  
    \\centering  
    \\begin{tikzpicture}\[scale=0.8\]  
        \\draw\[thick\] (0,0) \-- (3,0) node\[midway, below\] {$y$} \-- (0,2.5) node\[midway, right\] {$12$} \-- cycle node\[midway, left\] {$x$};  
        \\node at (0.3,1.7) {$30^\\circ$};  
        \\draw (0,0) rectangle (0.15,0.15);  
    \\end{tikzpicture}  
\\end{minipage}  
\\begin{minipage}\[t\]{0.65\\textwidth}  
    \\begin{align\*}  
        Sen\\,30^\\circ &= \\frac{y}{12} \\\\  
        12 \\cdot (0.5) &= y \\\\  
        \\mathbf{y} &= \\mathbf{6} \\\\  
        Cos\\,30^\\circ &= \\frac{x}{12} \\\\  
        12 \\cdot (0.866) &= x \\\\  
        \\mathbf{x} &= \\mathbf{10.39} \\\\  
        \\alpha &= 180 \- 90 \- 30 \\\\  
        \\mathbf{\\alpha} &= \\mathbf{60^\\circ}  
    \\end{align\*}  
\\end{minipage}

\\vspace{1em}  
\\hrule  
\\vspace{1em}

\\noindent  
\\begin{minipage}\[t\]{0.35\\textwidth}  
    \\centering  
    \\begin{tikzpicture}\[scale=0.8\]  
        \\draw\[thick\] (0,0) \-- (3.5,0) node\[midway, below\] {$b$} \-- (0,1.5) node\[midway, right\] {$z$} \-- cycle node\[midway, left\] {$10$};  
        \\node at (0.3,0.8) {$14^\\circ$};  
        \\draw (0,0) rectangle (0.15,0.15);  
    \\end{tikzpicture}  
\\end{minipage}  
\\begin{minipage}\[t\]{0.65\\textwidth}  
    \\begin{align\*}  
        Tan\\,14^\\circ &= \\frac{b}{10} \\\\  
        10 \\cdot (0.249) &= b \\\\  
        \\mathbf{b} &= \\mathbf{2.49} \\\\  
        Cos\\,14^\\circ &= \\frac{10}{z} \\\\  
        z &= \\frac{10}{0.970} \\\\  
        \\mathbf{z} &= \\mathbf{10.31} \\\\  
        \\alpha &= 180 \- 90 \- 14 \\\\  
        \\mathbf{\\alpha} &= \\mathbf{76^\\circ}  
    \\end{align\*}  
\\end{minipage}  
% \--- FIN\_SECCION: RESOLUCIONES \---

\\vspace{1em}  
\\hrule  
\\vspace{1em}

% \--- INICIO\_SECCION: EXTRAS \---  
\\section\*{\\centering Ejercicios Extras}

\\noindent  
\\begin{minipage}\[t\]{0.33\\textwidth}  
    \\centering  
    \\begin{tikzpicture}\[scale=0.8\]  
        \\draw\[thick\] (0,0) \-- (2,0) node\[midway, below\] {$x$} \-- (0,3) node\[midway, right\] {$y$} \-- cycle node\[midway, left\] {$12$};  
        \\node at (1.3,0.3) {$30^\\circ$};  
        \\draw (0,0) rectangle (0.2,0.2);  
    \\end{tikzpicture}  
\\end{minipage}  
\\begin{minipage}\[t\]{0.33\\textwidth}  
    \\centering  
    \\begin{tikzpicture}\[scale=0.8\]  
        \\draw\[thick\] (0,0) \-- (3,0) node\[midway, below\] {$y$} \-- (0,3) node\[midway, right\] {$z$} \-- cycle node\[midway, left\] {$8$};  
        \\node at (2.2,0.3) {$45^\\circ$};  
        \\draw (0,0) rectangle (0.2,0.2);  
    \\end{tikzpicture}  
\\end{minipage}  
\\begin{minipage}\[t\]{0.33\\textwidth}  
    \\centering  
    \\begin{tikzpicture}\[scale=0.8\]  
        \\draw\[thick\] (0,0) \-- (2.5,0) node\[midway, below\] {$7$} \-- (0,3.5) node\[midway, right\] {$15$} \-- cycle node\[midway, left\] {$x$};  
        \\node at (1.8,0.3) {$\\alpha$};  
        \\draw (0,0) rectangle (0.2,0.2);  
    \\end{tikzpicture}  
\\end{minipage}

\\vspace{2em}

\\noindent  
\\begin{minipage}\[t\]{0.33\\textwidth}  
    \\centering  
    \\begin{tikzpicture}\[scale=0.8\]  
        \\draw\[thick\] (0,0) \-- (3,0) node\[midway, below\] {$4$} \-- (0,2) node\[midway, right\] {$a$} \-- cycle node\[midway, left\] {$y$};  
        \\node at (2.2,0.3) {$22^\\circ$};  
        \\draw (0,0) rectangle (0.2,0.2);  
    \\end{tikzpicture}  
\\end{minipage}  
\\begin{minipage}\[t\]{0.33\\textwidth}  
    \\centering  
    \\begin{tikzpicture}\[scale=0.8\]  
        \\draw\[thick\] (0,0) \-- (2,0) node\[midway, below\] {$10$} \-- (0,3) node\[midway, right\] {$h$} \-- cycle node\[midway, left\] {$b$};  
        \\node at (1.3,0.3) {$50^\\circ$};  
        \\draw (0,0) rectangle (0.2,0.2);  
    \\end{tikzpicture}  
\\end{minipage}  
\\begin{minipage}\[t\]{0.33\\textwidth}  
    \\centering  
    \\begin{tikzpicture}\[scale=0.8\]  
        \\draw\[thick\] (0,0) \-- (3,0) node\[midway, below\] {$c$} \-- (0,1.5) node\[midway, right\] {$18$} \-- cycle node\[midway, left\] {$12$};  
        \\node at (0.3,1) {$\\beta$};  
        \\draw (0,0) rectangle (0.2,0.2);  
    \\end{tikzpicture}  
\\end{minipage}  
% \--- FIN\_SECCION: EXTRAS \---

\\end{document}

# 11 semejanza de triángulos

\\documentclass\[11pt\]{article}  
\\usepackage\[margin=1.5cm\]{geometry}  
\\usepackage{fontspec}  
\\setmainfont{Noto Sans}  
\\usepackage{amsmath, amssymb}  
\\usepackage{enumitem}  
\\usepackage{tikz}  
\\pagestyle{empty}

% Configuración para listas sin numeración ni viñetas  
\\setlist\[itemize\]{label={}, leftmargin=0pt, itemsep=1.5em}

\\begin{document}

% Título principal centrado con línea separadora  
\\begin{center}  
    {\\Huge \\textbf{Semejanza}} \\\\  
    \\vspace{0.5em}  
    \\hrule  
\\end{center}

\\vspace{1em}

% \--- INICIO\_SECCION: MINI APUNTE \---  
\\section\*{\\centering Mini Apunte}  
Decimos que dos triángulos son semejantes cuando tienen la misma forma, aunque sus tamaños sean diferentes. Esto significa que sus ángulos son iguales y sus lados son proporcionales. Cuando un triángulo está dentro de otro, podemos encontrar medidas desconocidas usando la relación: $\\frac{\\text{Altura}}{\\text{Base}} \= \\frac{\\text{altura}}{\\text{base}}$.  
% \--- FIN\_SECCION: MINI APUNTE \---

\\vspace{1em}  
\\rule{\\textwidth}{0.4pt}  
\\vspace{1em}

% \--- INICIO\_SECCION: EJEMPLOS \---  
\\section\*{\\centering Ejemplos}

% PARTE 1: Proporciones  
\\begin{center}  
    \\begin{tikzpicture}\[scale=0.7\]  
        \\draw\[thick\] (0,0) \-- (3,0) node\[midway, below\]{$b$} \-- (1,2) node\[midway, right\]{$z$} \-- cycle node\[midway, left\]{$a$};  
    \\end{tikzpicture}  
    \\quad  
    \\begin{tikzpicture}\[scale=1\]  
        \\draw\[thick\] (0,0) \-- (3,0) node\[midway, below\]{$c$} \-- (1,2) node\[midway, right\]{$x$} \-- cycle node\[midway, left\]{$y$};  
    \\end{tikzpicture}  
      
    \\vspace{1em}  
    \\textbf{Escribe seis proporciones:}  
    \\begin{align\*}  
        \\frac{a}{b} &= \\frac{y}{c} & \\frac{b}{c} &= \\frac{a}{y} \\\\  
        \\frac{z}{a} &= \\frac{x}{y} & \\frac{a}{y} &= \\frac{z}{x} \\\\  
        \\frac{x}{c} &= \\frac{z}{b} & \\frac{x}{z} &= \\frac{c}{b}  
    \\end{align\*}  
\\end{center}

\\vspace{1em}  
\\rule{0.6\\textwidth}{0.2pt}  
\\vspace{1em}

% PARTE 2: Figuras con enunciado y separación  
\\noindent  
\\begin{minipage}\[t\]{0.48\\textwidth}  
    \\centering  
    Calcula el valor de $x$  
    \\vspace{1em}  
      
    \\begin{tikzpicture}\[scale=0.12\]  
        \\draw\[thick\] (0,0) \-- (12,0) \-- (0,15) \-- cycle;  
        \\draw\[thick\] (8,0) \-- (8,5);  
        \\node\[left\] at (0,7.5) {$x$};  
        \\node\[below\] at (6,0) {$12$};  
        \\node\[right\] at (8,2.5) {$6$};  
        \\node\[below\] at (10,0) {$8$};  
    \\end{tikzpicture}  
      
    \\vspace{0.8em}  
    % Separación de triángulos para x  
    \\begin{tikzpicture}\[scale=0.08\]  
        \\draw\[thick\] (0,0) \-- (12,0) \-- (0,15) \-- cycle;  
        \\node\[left\] at (0,7.5) {$x$};  
        \\node\[below\] at (6,0) {$12$};  
    \\end{tikzpicture}  
    \\quad  
    \\begin{tikzpicture}\[scale=0.08\]  
        \\draw\[thick\] (0,0) \-- (8,0) \-- (0,10) \-- cycle;  
        \\node\[left\] at (0,5) {$6$};  
        \\node\[below\] at (4,0) {$8$};  
    \\end{tikzpicture}

    \\begin{align\*}  
        \\frac{x}{12} &= \\frac{6}{8} \\\\  
        8x &= 6(12) \\\\  
        8x &= 72 \\\\  
        x &= \\frac{72}{8} \\\\  
        \\mathbf{x \= 9}  
    \\end{align\*}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.48\\textwidth}  
    \\centering  
    Calcula el valor de $y$  
    \\vspace{1em}  
      
    \\begin{tikzpicture}\[scale=0.12\]  
        \\draw\[thick\] (0,0) \-- (10,0) \-- (0,8) \-- cycle;  
        \\draw\[thick\] (5,0) \-- (5,4);  
        \\node\[left\] at (0,4) {$8$};  
        \\node\[below\] at (5,0) {$10$};  
        \\node\[below\] at (2.5,0) {$y$};  
        \\node\[right\] at (5,2) {$5$};  
    \\end{tikzpicture}  
      
    \\vspace{0.8em}  
    % Separación de triángulos para y  
    \\begin{tikzpicture}\[scale=0.08\]  
        \\draw\[thick\] (0,0) \-- (16,0) \-- (0,12.8) \-- cycle;  
        \\node\[left\] at (0,6.4) {$8$};  
        \\node\[below\] at (8,0) {$y$};  
    \\end{tikzpicture}  
    \\quad  
    \\begin{tikzpicture}\[scale=0.08\]  
        \\draw\[thick\] (0,0) \-- (10,0) \-- (0,8) \-- cycle;  
        \\node\[left\] at (0,4) {$5$};  
        \\node\[below\] at (5,0) {$10$};  
    \\end{tikzpicture}

    \\begin{align\*}  
        \\frac{y}{10} &= \\frac{8}{5} \\\\  
        5y &= 8(10) \\\\  
        5y &= 80 \\\\  
        y &= \\frac{80}{5} \\\\  
        \\mathbf{y \= 16}  
    \\end{align\*}  
\\end{minipage}

\\vspace{1em}  
\\rule{0.6\\textwidth}{0.2pt}  
\\vspace{1em}

% PARTE 3: Problema  
\\noindent  
Calcula la altura de un edificio que da una sombra de $8.5$ m si a la misma hora un poste de altura $2.3$ m da una sombra de $1.5$ m.

\\begin{center}  
    \\begin{tikzpicture}\[scale=0.15\]  
        \\draw\[thick\] (0,0) \-- (8.5,0) \-- (0,12) \-- cycle;  
        \\node\[left\] at (0,6) {$X$};  
        \\node\[below\] at (4.25,0) {$8.5$};  
    \\end{tikzpicture}  
    \\quad  
    \\begin{tikzpicture}\[scale=0.25\]  
        \\draw\[thick\] (0,0) \-- (1.5,0) \-- (0,2.3) \-- cycle;  
        \\node\[left\] at (0,1.15) {$2.3$};  
        \\node\[below\] at (0.75,0) {$1.5$};  
    \\end{tikzpicture}  
\\end{center}

\\begin{align\*}  
    \\frac{X}{8.5} &= \\frac{2.3}{1.5} \\\\  
    1.5X &= 2.3(8.5) \\\\  
    1.5X &= 19.55 \\\\  
    X &= \\frac{19.55}{1.5} \\\\  
    \\mathbf{X \\approx 13.03}  
\\end{align\*}  
% \--- FIN\_SECCION: EJEMPLOS \---

\\vspace{1em}  
\\rule{\\textwidth}{0.4pt}  
\\vspace{1em}

% \--- INICIO\_SECCION: EJERCICIOS \---  
\\section\*{\\centering Ejercicios}

\\begin{center}\\textbf{\\large Bloque 1}\\end{center}  
\\noindent  
\\begin{minipage}\[t\]{0.3\\textwidth}  
    \\centering  
    Escribe seis proporciones  
    \\vspace{0.5em}  
    \\begin{tikzpicture}\[scale=0.4\]  
        \\draw\[thick\] (0,0) \-- (3,1) node\[midway, below\]{$a$} \-- (1,2) node\[midway, right\]{$y$} \-- cycle node\[midway, left\]{$x$};  
    \\end{tikzpicture}  
    \\begin{tikzpicture}\[scale=0.4\]  
        \\draw\[thick\] (0,0) \-- (3,1) node\[midway, below\]{$c$} \-- (1,2) node\[midway, right\]{$z$} \-- cycle node\[midway, left\]{$b$};  
    \\end{tikzpicture}  
\\end{minipage}  
\\begin{minipage}\[t\]{0.35\\textwidth}  
    \\centering  
    Calcula los valores de $x$ e $y$  
    \\vspace{0.5em}  
    \\begin{tikzpicture}\[scale=0.1\]  
        \\draw\[thick\] (0,0) \-- (10,0) \-- (0,12) \-- cycle;  
        \\draw\[thick\] (4,0) \-- (4,7.2);  
        \\node\[left\] at (0,6) {$10$};  
        \\node\[below\] at (2,0) {$y$};  
        \\node\[below\] at (7,0) {$4$};  
        \\node\[right\] at (4,3.6) {$7$};  
    \\end{tikzpicture}  
    \\begin{tikzpicture}\[scale=0.1\]  
        \\draw\[thick\] (0,0) \-- (12,0) \-- (0,15) \-- cycle;  
        \\draw\[thick\] (7,0) \-- (7,6.25);  
        \\node\[left\] at (0,7.5) {$x$};  
        \\node\[below\] at (3.5,0) {$12$};  
        \\node\[below\] at (9.5,0) {$5$};  
        \\node\[right\] at (7,3.1) {$7$};  
    \\end{tikzpicture}  
\\end{minipage}  
\\begin{minipage}\[t\]{0.3\\textwidth}  
    Calcula la altura de un edificio con sombra de $7.2$ m si un poste de $3.4$ m tiene sombra de $1.3$ m.  
\\end{minipage}

\\vspace{1.5em}

\\begin{center}\\textbf{\\large Bloque 2}\\end{center}  
\\noindent  
\\begin{minipage}\[t\]{0.3\\textwidth}  
    \\centering  
    Escribe seis proporciones  
    \\vspace{0.5em}  
    \\begin{tikzpicture}\[scale=0.4\]  
        \\draw\[thick\] (0,0) \-- (4,0) node\[midway, below\]{$z$} \-- (1,2) node\[midway, right\]{$y$} \-- cycle node\[midway, left\]{$a$};  
    \\end{tikzpicture}  
    \\begin{tikzpicture}\[scale=0.35\]  
        \\draw\[thick\] (0,0) \-- (4,0) node\[midway, below\]{$c$} \-- (1,2) node\[midway, right\]{$x$} \-- cycle node\[midway, left\]{$b$};  
    \\end{tikzpicture}  
\\end{minipage}  
\\begin{minipage}\[t\]{0.35\\textwidth}  
    \\centering  
    Calcula los valores de $x$ e $y$  
    \\vspace{0.5em}  
    \\begin{tikzpicture}\[scale=0.08\]  
        \\draw\[thick\] (0,0) \-- (15,0) \-- (0,12) \-- cycle;  
        \\draw\[thick\] (6,0) \-- (6,7.2);  
        \\node\[left\] at (0,6) {$x$};  
        \\node\[below\] at (3,0) {$15$};  
        \\node\[below\] at (10.5,0) {$9$};  
        \\node\[right\] at (6,3.6) {$8$};  
    \\end{tikzpicture}  
    \\begin{tikzpicture}\[scale=0.1\]  
        \\draw\[thick\] (0,0) \-- (8,0) \-- (0,14) \-- cycle;  
        \\draw\[thick\] (2,0) \-- (2,10.5);  
        \\node\[left\] at (0,7) {$14$};  
        \\node\[below\] at (1,0) {$8$};  
        \\node\[below\] at (5,0) {$6$};  
        \\node\[right\] at (2,5.25) {$x$};  
    \\end{tikzpicture}  
\\end{minipage}  
\\begin{minipage}\[t\]{0.3\\textwidth}  
    Calcula la altura de un edificio con sombra de $6.5$ m si un poste de $2.7$ m tiene sombra de $1.4$ m.  
\\end{minipage}  
% \--- FIN\_SECCION: EJERCICIOS \---

\\newpage

% \--- INICIO\_SECCION: EJERCICIOS RESUELTOS \---  
\\section\*{\\centering Ejercicios Resueltos}

\\begin{center}\\textbf{\\large Bloque 1}\\end{center}

\\noindent  
\\begin{minipage}\[t\]{0.3\\textwidth}  
    \\centering  
    \\begin{tikzpicture}\[scale=0.3\]  
        \\draw\[thick\] (0,0) \-- (3,1) node\[midway, below, scale=0.6\]{$a$} \-- (1,2) node\[midway, right, scale=0.6\]{$y$} \-- cycle node\[midway, left, scale=0.6\]{$x$};  
        \\draw\[thick\] (4,0) \-- (7,1) node\[midway, below, scale=0.6\]{$c$} \-- (5,2) node\[midway, right, scale=0.6\]{$z$} \-- cycle node\[midway, left, scale=0.6\]{$b$};  
    \\end{tikzpicture}  
    \\begin{align\*}  
        \\frac{x}{a} &= \\frac{b}{c} \\\\  
        \\frac{y}{a} &= \\frac{z}{c} \\\\  
        \\frac{x}{y} &= \\frac{b}{z} \\\\  
        \\frac{a}{x} &= \\frac{c}{b} \\\\  
        \\frac{a}{y} &= \\frac{c}{z} \\\\  
        \\frac{y}{x} &= \\frac{z}{b}  
    \\end{align\*}  
\\end{minipage}  
\\begin{minipage}\[t\]{0.35\\textwidth}  
    \\centering  
    \\begin{tikzpicture}\[scale=0.08\]  
        \\draw\[thick\] (0,0) \-- (10,0) \-- (0,12) \-- cycle;  
        \\draw\[thick\] (4,0) \-- (4,7.2);  
        \\node\[left, scale=0.6\] at (0,6) {$10$};  
        \\node\[below, scale=0.6\] at (2,0) {$y$};  
        \\node\[below, scale=0.6\] at (7,0) {$4$};  
        \\node\[right, scale=0.6\] at (4,3.6) {$7$};  
    \\end{tikzpicture}  
    \\begin{align\*}  
        \\frac{10}{y} &= \\frac{7}{4} \\\\  
        7y &= 4(10) \\\\  
        7y &= 40 \\\\  
        y &= \\frac{40}{7} \\\\  
        \\mathbf{y \\approx 5.71}  
    \\end{align\*}  
\\end{minipage}  
\\begin{minipage}\[t\]{0.3\\textwidth}  
    \\centering  
    \\phantom{x}  
    \\vspace{1.5em}  
    \\begin{tikzpicture}\[scale=0.08\]  
        \\draw\[thick\] (0,0) \-- (12,0) \-- (0,15) \-- cycle;  
        \\draw\[thick\] (7,0) \-- (7,6.25);  
        \\node\[left, scale=0.6\] at (0,7.5) {$x$};  
        \\node\[below, scale=0.6\] at (3.5,0) {$12$};  
        \\node\[below, scale=0.6\] at (9.5,0) {$5$};  
        \\node\[right, scale=0.6\] at (7,3.1) {$7$};  
    \\end{tikzpicture}  
    \\begin{align\*}  
        \\frac{x}{12} &= \\frac{7}{5} \\\\  
        5x &= 7(12) \\\\  
        5x &= 84 \\\\  
        x &= \\frac{84}{5} \\\\  
        \\mathbf{x \= 16.8}  
    \\end{align\*}  
\\end{minipage}

\\vspace{1.5em}  
\\noindent  
Calcula la altura de un edificio con sombra de $7.2$ m si un poste de $3.4$ m tiene sombra de $1.3$ m.  
\\begin{center}  
    \\begin{tikzpicture}\[scale=0.15\]  
        \\draw\[thick\] (0,0) \-- (7.2,0) \-- (0,18.83) \-- cycle;  
        \\node\[left\] at (0,9.4) {$h$};  
        \\node\[below\] at (3.6,0) {$7.2$};  
    \\end{tikzpicture}  
    \\quad  
    \\begin{tikzpicture}\[scale=0.25\]  
        \\draw\[thick\] (0,0) \-- (1.3,0) \-- (0,3.4) \-- cycle;  
        \\node\[left\] at (0,1.7) {$3.4$};  
        \\node\[below\] at (0.65,0) {$1.3$};  
    \\end{tikzpicture}  
\\end{center}  
\\begin{align\*}  
    \\frac{h}{7.2} &= \\frac{3.4}{1.3} \\\\  
    1.3h &= 3.4(7.2) \\\\  
    1.3h &= 24.48 \\\\  
    h &= \\frac{24.48}{1.3} \\\\  
    \\mathbf{h \\approx 18.83}  
\\end{align\*}

\\vspace{1em}  
\\hrule  
\\vspace{1.5em}

\\begin{center}\\textbf{\\large Bloque 2}\\end{center}

\\noindent  
\\begin{minipage}\[t\]{0.3\\textwidth}  
    \\centering  
    \\begin{tikzpicture}\[scale=0.3\]  
        \\draw\[thick\] (0,0) \-- (4,0) node\[midway, below, scale=0.6\]{$z$} \-- (1,2) node\[midway, right, scale=0.6\]{$y$} \-- cycle node\[midway, left, scale=0.6\]{$a$};  
        \\draw\[thick\] (5,0) \-- (9,0) node\[midway, below, scale=0.6\]{$c$} \-- (6,2) node\[midway, right, scale=0.6\]{$x$} \-- cycle node\[midway, left, scale=0.6\]{$b$};  
    \\end{tikzpicture}  
    \\begin{align\*}  
        \\frac{a}{z} &= \\frac{b}{c} \\\\  
        \\frac{y}{z} &= \\frac{x}{c} \\\\  
        \\frac{a}{y} &= \\frac{b}{x} \\\\  
        \\frac{z}{a} &= \\frac{c}{b} \\\\  
        \\frac{z}{y} &= \\frac{c}{x} \\\\  
        \\frac{y}{a} &= \\frac{x}{b}  
    \\end{align\*}  
\\end{minipage}  
\\begin{minipage}\[t\]{0.35\\textwidth}  
    \\centering  
    \\begin{tikzpicture}\[scale=0.08\]  
        \\draw\[thick\] (0,0) \-- (15,0) \-- (0,12) \-- cycle;  
        \\draw\[thick\] (6,0) \-- (6,7.2);  
        \\node\[left, scale=0.6\] at (0,6) {$x$};  
        \\node\[below, scale=0.6\] at (3,0) {$15$};  
        \\node\[below, scale=0.6\] at (10.5,0) {$9$};  
        \\node\[right, scale=0.6\] at (6,3.6) {$8$};  
    \\end{tikzpicture}  
    \\begin{align\*}  
        \\frac{x}{15} &= \\frac{8}{9} \\\\  
        9x &= 8(15) \\\\  
        9x &= 120 \\\\  
        x &= \\frac{120}{9} \\\\  
        \\mathbf{x \\approx 13.33}  
    \\end{align\*}  
\\end{minipage}  
\\begin{minipage}\[t\]{0.3\\textwidth}  
    \\centering  
    \\phantom{x}  
    \\vspace{1.5em}  
    \\begin{tikzpicture}\[scale=0.08\]  
        \\draw\[thick\] (0,0) \-- (8,0) \-- (0,14) \-- cycle;  
        \\draw\[thick\] (2,0) \-- (2,10.5);  
        \\node\[left, scale=0.6\] at (0,7) {$14$};  
        \\node\[below, scale=0.6\] at (1,0) {$8$};  
        \\node\[below, scale=0.6\] at (5,0) {$6$};  
        \\node\[right, scale=0.6\] at (2,5.25) {$x$};  
    \\end{tikzpicture}  
    \\begin{align\*}  
        \\frac{14}{8} &= \\frac{x}{6} \\\\  
        8x &= 14(6) \\\\  
        8x &= 84 \\\\  
        x &= \\frac{84}{8} \\\\  
        \\mathbf{x \= 10.5}  
    \\end{align\*}  
\\end{minipage}

\\vspace{1.5em}  
\\noindent  
Calcula la altura de un edificio con sombra de $6.5$ m si un poste de $2.7$ m tiene sombra de $1.4$ m.  
\\begin{center}  
    \\begin{tikzpicture}\[scale=0.15\]  
        \\draw\[thick\] (0,0) \-- (6.5,0) \-- (0,12.53) \-- cycle;  
        \\node\[left\] at (0,6.2) {$h$};  
        \\node\[below\] at (3.25,0) {$6.5$};  
    \\end{tikzpicture}  
    \\quad  
    \\begin{tikzpicture}\[scale=0.25\]  
        \\draw\[thick\] (0,0) \-- (1.4,0) \-- (0,2.7) \-- cycle;  
        \\node\[left\] at (0,1.35) {$2.7$};  
        \\node\[below\] at (0.7,0) {$1.4$};  
    \\end{tikzpicture}  
\\end{center}  
\\begin{align\*}  
    \\frac{h}{6.5} &= \\frac{2.7}{1.4} \\\\  
    1.4h &= 2.7(6.5) \\\\  
    1.4h &= 17.55 \\\\  
    h &= \\frac{17.55}{1.4} \\\\  
    \\mathbf{h \\approx 12.53}  
\\end{align\*}  
% \--- FIN\_SECCION: EJERCICIOS RESUELTOS \---

\\newpage

% \--- INICIO\_SECCION: EXTRAS \---  
\\section\*{\\centering Ejercicios Extras}

\\noindent  
\\begin{minipage}\[t\]{0.3\\textwidth}  
    \\centering  
    Escribe seis proporciones  
    \\vspace{0.5em}  
    \\begin{tikzpicture}\[scale=0.4\]  
        \\draw\[thick\] (0,0) \-- (3,0) node\[midway, below\]{$m$} \-- (1,2) node\[midway, right\]{$p$} \-- cycle node\[midway, left\]{$n$};  
    \\end{tikzpicture}  
    \\begin{tikzpicture}\[scale=0.4\]  
        \\draw\[thick\] (0,0) \-- (3,0) node\[midway, below\]{$r$} \-- (1,2) node\[midway, right\]{$t$} \-- cycle node\[midway, left\]{$s$};  
    \\end{tikzpicture}  
\\end{minipage}  
\\begin{minipage}\[t\]{0.35\\textwidth}  
    \\centering  
    Calcula el valor de $x$  
    \\vspace{0.5em}  
    \\begin{tikzpicture}\[scale=0.1\]  
        \\draw\[thick\] (0,0) \-- (15,0) \-- (0,20) \-- cycle;  
        \\draw\[thick\] (6,0) \-- (6,12);  
        \\node\[left\] at (0,10) {$20$};  
        \\node\[below\] at (3,0) {$x$};  
        \\node\[below\] at (10.5,0) {$15$};  
        \\node\[right\] at (6,6) {$12$};  
    \\end{tikzpicture}  
\\end{minipage}  
\\begin{minipage}\[t\]{0.3\\textwidth}  
    Calcula la sombra de un árbol de $15$ m si un poste de $1.2$ m tiene sombra de $0.8$ m.  
\\end{minipage}

\\vspace{1.5em}  
\\rule{0.6\\textwidth}{0.2pt}  
\\vspace{1.5em}

\\noindent  
\\begin{minipage}\[t\]{0.3\\textwidth}  
    \\centering  
    Calcula los valores de $x$ e $y$  
    \\vspace{0.5em}  
    \\begin{tikzpicture}\[scale=0.4\]  
        \\draw\[thick\] (0,0) \-- (2,0) node\[midway, below\]{$4$} \-- (0,3) node\[midway, left\]{$3$} \-- cycle node\[midway, right\]{$5$};  
    \\end{tikzpicture}  
    \\begin{tikzpicture}\[scale=0.5\]  
        \\draw\[thick\] (0,0) \-- (2,0) node\[midway, below\]{$y$} \-- (0,3) node\[midway, left\]{$x$} \-- cycle node\[midway, right\]{$10$};  
    \\end{tikzpicture}  
\\end{minipage}  
\\begin{minipage}\[t\]{0.35\\textwidth}  
    \\centering  
    Calcula el valor de $h$  
    \\vspace{0.5em}  
    \\begin{tikzpicture}\[scale=0.08\]  
        \\draw\[thick\] (0,0) \-- (30,0) \-- (0,24) \-- cycle;  
        \\draw\[thick\] (10,0) \-- (10,16);  
        \\node\[left\] at (0,12) {$h$};  
        \\node\[below\] at (5,0) {$10$};  
        \\node\[below\] at (20,0) {$30$};  
        \\node\[right\] at (10,8) {$12$};  
    \\end{tikzpicture}  
\\end{minipage}  
\\begin{minipage}\[t\]{0.3\\textwidth}  
    Un edificio de $40$ m tiene una sombra de $25$ m. ¿Qué altura tiene un árbol con sombra de $5$ m?  
\\end{minipage}

\\vspace{1.5em}  
\\rule{0.6\\textwidth}{0.2pt}  
\\vspace{1.5em}

\\noindent  
\\begin{minipage}\[t\]{0.3\\textwidth}  
    \\centering  
    Escribe seis proporciones  
    \\vspace{0.5em}  
    \\begin{tikzpicture}\[scale=0.4\]  
        \\draw\[thick\] (0,0) \-- (2,2) node\[midway, left\]{$a$} \-- (4,0) node\[midway, right\]{$b$} \-- cycle node\[midway, below\]{$c$};  
    \\end{tikzpicture}  
    \\begin{tikzpicture}\[scale=0.6\]  
        \\draw\[thick\] (0,0) \-- (2,2) node\[midway, left\]{$2a$} \-- (4,0) node\[midway, right\]{$2b$} \-- cycle node\[midway, below\]{$2c$};  
    \\end{tikzpicture}  
\\end{minipage}  
\\begin{minipage}\[t\]{0.35\\textwidth}  
    \\centering  
    Calcula el valor de $x$  
    \\vspace{0.5em}  
    \\begin{tikzpicture}\[scale=0.1\]  
        \\draw\[thick\] (0,0) \-- (12,0) \-- (0,15) \-- cycle;  
        \\draw\[thick\] (4,0) \-- (4,10);  
        \\node\[left\] at (0,7.5) {$15$};  
        \\node\[below\] at (2,0) {$4$};  
        \\node\[below\] at (8,0) {$x$};  
        \\node\[right\] at (4,5) {$10$};  
    \\end{tikzpicture}  
\\end{minipage}  
\\begin{minipage}\[t\]{0.3\\textwidth}  
    Una persona de $1.75$ m proyecta una sombra de $2.1$ m. Calcula la sombra de un edificio de $12$ m.  
\\end{minipage}

\\vspace{1.5em}  
\\rule{0.6\\textwidth}{0.2pt}  
\\vspace{1.5em}

\\noindent  
\\begin{minipage}\[t\]{0.3\\textwidth}  
    \\centering  
    Calcula el valor de $x$  
    \\vspace{0.5em}  
    \\begin{tikzpicture}\[scale=0.4\]  
        \\draw\[thick\] (0,0) \-- (4,0) node\[midway, below\]{$8$} \-- (0,2) node\[midway, left\]{$x$} \-- cycle;  
    \\end{tikzpicture}  
    \\begin{tikzpicture}\[scale=0.2\]  
        \\draw\[thick\] (0,0) \-- (4,0) node\[midway, below\]{$2$} \-- (0,2) node\[midway, left\]{$4$} \-- cycle;  
    \\end{tikzpicture}  
\\end{minipage}  
\\begin{minipage}\[t\]{0.35\\textwidth}  
    \\centering  
    Calcula el valor de $y$  
    \\vspace{0.5em}  
    \\begin{tikzpicture}\[scale=0.08\]  
        \\draw\[thick\] (0,0) \-- (18,0) \-- (0,24) \-- cycle;  
        \\draw\[thick\] (12,0) \-- (12,8);  
        \\node\[left\] at (0,12) {$24$};  
        \\node\[below\] at (6,0) {$18$};  
        \\node\[below\] at (15,0) {$y$};  
        \\node\[right\] at (12,4) {$16$};  
    \\end{tikzpicture}  
\\end{minipage}  
\\begin{minipage}\[t\]{0.3\\textwidth}  
    Un faro proyecta una sombra de $30$ m. Un poste de $2.5$ m proyecta una sombra de $1.8$ m. Calcula la altura del faro.  
\\end{minipage}  
% \--- FIN\_SECCION: EXTRAS \---

\\end{document}

# 12 proporcionalidad regla de tres

\\documentclass\[11pt\]{article}  
\\usepackage\[margin=1.5cm\]{geometry}  
\\usepackage{fontspec}  
\\setmainfont{Noto Sans}  
\\usepackage{amsmath, amssymb}  
\\usepackage{enumitem}  
\\usepackage{tikz}  
\\pagestyle{empty}

\\begin{document}

% \--- INICIO\_SECCION: TITULO \---  
\\begin{center}  
    {\\Huge \\textbf{Proporcionalidad}} \\\\  
    \\vspace{0.5em}  
    \\hrule  
\\end{center}  
% \--- FIN\_SECCION: TITULO \---

\\vspace{1em}

% \--- INICIO\_SECCION: MINI\_APUNTE \---  
\\section\*{\\centering Regla de Tres}

\\noindent  
\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{center}\\textbf{\\large Proporcionalidad Directa}\\end{center}  
    Cuando una magnitud aumenta, la otra también aumenta.  
    \\begin{center}  
        \\fbox{  
            \\begin{tabular}{c}  
                $A \\rightarrow B$ \\\\  
                $C \\rightarrow X$  
            \\end{tabular}  
        }  
    \\end{center}  
    \\begin{align\*}  
        X &= \\frac{C \\cdot B}{A}  
    \\end{align\*}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{center}\\textbf{\\large Proporcionalidad Indirecta}\\end{center}  
    Cuando una magnitud aumenta, la otra disminuye.  
    \\begin{center}  
        \\fbox{  
            \\begin{tabular}{c}  
                $A \\rightarrow B$ \\\\  
                $C \\rightarrow X$  
            \\end{tabular}  
        }  
    \\end{center}  
    \\begin{align\*}  
        X &= \\frac{A \\cdot B}{C}  
    \\end{align\*}  
\\end{minipage}

\\vspace{1em}  
\\hrule  
\\vspace{1em}  
% \--- FIN\_SECCION: MINI\_APUNTE \---

% \--- INICIO\_SECCION: EJEMPLOS \---  
\\section\*{\\centering Ejemplos}

\\noindent  
\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{itemize}\[label={}, leftmargin=0pt\]  
        \\item Calcula el $12\\%$ de $320$  
        \\begin{center}  
            \\fbox{  
                \\begin{tabular}{c}  
                    $320 \\rightarrow 100\\%$ \\\\  
                    $X \\rightarrow 12\\%$  
                \\end{tabular}  
            }  
        \\end{center}  
        \\begin{align\*}  
            X &= \\frac{12(320)}{100} \\\\  
            X &= \\frac{3840}{100} \\\\  
            X &= \\mathbf{38.4}  
        \\end{align\*}  
        \\item Si $3$ kg de mango cuestan $\\$100$ ¿cuánto podría comprar con $\\$250$?  
        \\begin{center}  
            \\fbox{  
                \\begin{tabular}{c}  
                    $3\\text{ kg} \\rightarrow \\$100$ \\\\  
                    $X \\rightarrow \\$250$  
                \\end{tabular}  
            }  
        \\end{center}  
        \\begin{align\*}  
            X &= \\frac{250(3)}{100} \\\\  
            X &= \\frac{750}{100} \\\\  
            X &= \\mathbf{7.5 \\text{ kg}}  
        \\end{align\*}  
    \\end{itemize}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{itemize}\[label={}, leftmargin=0pt\]  
        \\item Un celular costaba $\\$3200$. Si descontaron $\\$350$ ¿qué porcentaje descontaron?  
        \\begin{center}  
            \\fbox{  
                \\begin{tabular}{c}  
                    $100\\% \\rightarrow \\$3200$ \\\\  
                    $X \\rightarrow \\$350$  
                \\end{tabular}  
            }  
        \\end{center}  
        \\begin{align\*}  
            X &= \\frac{350(100)}{3200} \\\\  
            X &= \\frac{35000}{3200} \\\\  
            X &= \\mathbf{10.93\\%}  
        \\end{align\*}  
        \\item $7$ pintores pintan una casa en $4$ días. ¿Cuánto tiempo tardarán $10$ pintores?  
        \\begin{center}  
            \\fbox{  
                \\begin{tabular}{c}  
                    $7 \\rightarrow 4 \\text{ días}$ \\\\  
                    $10 \\rightarrow X$  
                \\end{tabular}  
            }  
        \\end{center}  
        \\begin{align\*}  
            X &= \\frac{7(4)}{10} \\\\  
            X &= \\frac{28}{10} \\\\  
            X &= \\mathbf{2.8 \\text{ días}}  
        \\end{align\*}  
    \\end{itemize}  
\\end{minipage}

\\vspace{1em}  
\\hrule  
\\vspace{1em}  
% \--- FIN\_SECCION: EJEMPLOS \---

% \--- INICIO\_SECCION: EJERCICIOS \---  
\\section\*{\\centering Ejercicios}

\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 1}\\end{center}  
    \\begin{itemize}\[label={}, leftmargin=0pt, itemsep=1.5em\]  
        \\item Calcula el $12\\%$ de $280$.  
        \\item Si $7$ kg de peras cuestan $\\$250$ ¿cuánto podría comprar con $\\$750$?  
        \\item $4$ trabajadores pintan una casa en $6$ días. ¿Cuánto tiempo tardarán $10$ trabajadores?  
        \\item Un vestido costaba $\\$1500$. Si descontaron $\\$400$ ¿cuál fue el porcentaje del descuento?  
    \\end{itemize}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 2}\\end{center}  
    \\begin{itemize}\[label={}, leftmargin=0pt, itemsep=1.5em\]  
        \\item Calcula el $18\\%$ de $350$.  
        \\item Si $3$ kg de mangos cuestan $\\$100$ ¿cuánto podría comprar con $\\$250$?  
        \\item $5$ jardineros podan el parque en $2$ días. ¿Cuánto tiempo tardarán $3$ jardineros?  
        \\item Un celular costaba $\\$3500$. Si descontaron $\\$250$ ¿cuál fue el porcentaje del descuento?  
    \\end{itemize}  
\\end{minipage}

\\vspace{2em}

\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 3}\\end{center}  
    \\begin{itemize}\[label={}, leftmargin=0pt, itemsep=1.5em\]  
        \\item Calcula el $45\\%$ de $132$.  
        \\item Si $8$ kg de manzanas cuestan $\\$450$ ¿cuánto podría comprar con $\\$1700$?  
        \\item $6$ jardineros podan el jardín en $3$ días. ¿Cuántos jardineros se requieren para podarlo en $2$ días?  
        \\item Una bocina costaba $\\$1300$. Si descontaron $\\$300$ ¿cuál fue el porcentaje del descuento?  
    \\end{itemize}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 4}\\end{center}  
    \\begin{itemize}\[label={}, leftmargin=0pt, itemsep=1.5em\]  
        \\item Calcula el $36\\%$ de $520$.  
        \\item Si $4$ kg de fresas cuestan $\\$190$ ¿cuánto podría comprar con $\\$300$?  
        \\item $5$ trabajadores pintan una casa en $3$ días. ¿Cuántos trabajadores se requieren para pintarla en $1$ día?  
        \\item Un pantalón costaba $\\$620$. Si descontaron $\\$300$ ¿cuál fue el porcentaje del descuento?  
    \\end{itemize}  
\\end{minipage}  
% \--- FIN\_SECCION: EJERCICIOS \---

\\newpage

% \--- INICIO\_SECCION: RESOLUCIONES \---  
\\section\*{\\centering Resoluciones}

\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 1}\\end{center}  
    \\begin{itemize}\[label={}, leftmargin=0pt\]  
        \\item Calcula el $12\\%$ de $280$.  
        \\begin{center}  
            \\fbox{  
                \\begin{tabular}{c}  
                    $280 \\rightarrow 100\\%$ \\\\  
                    $X \\rightarrow 12\\%$  
                \\end{tabular}  
            }  
        \\end{center}  
        \\begin{align\*}  
            X &= \\frac{12(280)}{100} \\\\  
            X &= \\frac{3360}{100} \\\\  
            X &= \\mathbf{33.6}  
        \\end{align\*}  
        \\item Si $7$ kg de peras cuestan $\\$250$ ¿cuánto comprar con $750$?  
        \\begin{center}  
            \\fbox{  
                \\begin{tabular}{c}  
                    $7 \\text{ kg} \\rightarrow \\$250$ \\\\  
                    $X \\rightarrow \\$750$  
                \\end{tabular}  
            }  
        \\end{center}  
        \\begin{align\*}  
            X &= \\frac{750(7)}{250} \\\\  
            X &= \\frac{5250}{250} \\\\  
            X &= \\mathbf{21 \\text{ kg}}  
        \\end{align\*}  
        \\item $4$ trabajadores pintan una casa en $6$ días. ¿Cuánto tiempo tardarán $10$ trabajadores?  
        \\begin{center}  
            \\fbox{  
                \\begin{tabular}{c}  
                    $4 \\rightarrow 6 \\text{ días}$ \\\\  
                    $10 \\rightarrow X$  
                \\end{tabular}  
            }  
        \\end{center}  
        \\begin{align\*}  
            X &= \\frac{4(6)}{10} \\\\  
            X &= \\frac{24}{10} \\\\  
            X &= \\mathbf{2.4 \\text{ días}}  
        \\end{align\*}  
        \\item Un vestido costaba $\\$1500$. Si descontaron $\\$400$ ¿cuál fue el porcentaje del descuento?  
        \\begin{center}  
            \\fbox{  
                \\begin{tabular}{c}  
                    $100\\% \\rightarrow \\$1500$ \\\\  
                    $X \\rightarrow \\$400$  
                \\end{tabular}  
            }  
        \\end{center}  
        \\begin{align\*}  
            X &= \\frac{400(100)}{1500} \\\\  
            X &= \\frac{40000}{1500} \\\\  
            X &= \\mathbf{26.66\\%}  
        \\end{align\*}  
    \\end{itemize}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 2}\\end{center}  
    \\begin{itemize}\[label={}, leftmargin=0pt\]  
        \\item Calcula el $18\\%$ de $350$.  
        \\begin{center}  
            \\fbox{  
                \\begin{tabular}{c}  
                    $350 \\rightarrow 100\\%$ \\\\  
                    $X \\rightarrow 18\\%$  
                \\end{tabular}  
            }  
        \\end{center}  
        \\begin{align\*}  
            X &= \\frac{18(350)}{100} \\\\  
            X &= \\frac{6300}{100} \\\\  
            X &= \\mathbf{63}  
        \\end{align\*}  
        \\item Si $3$ kg de mangos cuestan $\\$100$ ¿cuánto comprar con $250$?  
        \\begin{center}  
            \\fbox{  
                \\begin{tabular}{c}  
                    $3 \\text{ kg} \\rightarrow \\$100$ \\\\  
                    $X \\rightarrow \\$250$  
                \\end{tabular}  
            }  
        \\end{center}  
        \\begin{align\*}  
            X &= \\frac{250(3)}{100} \\\\  
            X &= \\frac{750}{100} \\\\  
            X &= \\mathbf{7.5 \\text{ kg}}  
        \\end{align\*}  
        \\item $5$ jardineros podan el parque en $2$ días. ¿Cuánto tiempo tardarán 3 jardineros?  
        \\begin{center}  
            \\fbox{  
                \\begin{tabular}{c}  
                    $5 \\rightarrow 2 \\text{ días}$ \\\\  
                    $3 \\rightarrow X$  
                \\end{tabular}  
            }  
        \\end{center}  
        \\begin{align\*}  
            X &= \\frac{5(2)}{3} \\\\  
            X &= \\frac{10}{3} \\\\  
            X &= \\mathbf{3.33 \\text{ días}}  
        \\end{align\*}  
        \\item Un celular costaba $\\$3500$. Si descontaron $\\$250$ ¿cuál fue el porcentaje del descuento?  
        \\begin{center}  
            \\fbox{  
                \\begin{tabular}{c}  
                    $100\\% \\rightarrow \\$3500$ \\\\  
                    $X \\rightarrow \\$250$  
                \\end{tabular}  
            }  
        \\end{center}  
        \\begin{align\*}  
            X &= \\frac{250(100)}{3500} \\\\  
            X &= \\frac{25000}{3500} \\\\  
            X &= \\mathbf{7.14\\%}  
        \\end{align\*}  
    \\end{itemize}  
\\end{minipage}

\\newpage

\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 3}\\end{center}  
    \\begin{itemize}\[label={}, leftmargin=0pt\]  
        \\item Calcula el $45\\%$ de $132$.  
        \\begin{center}  
            \\fbox{  
                \\begin{tabular}{c}  
                    $132 \\rightarrow 100\\%$ \\\\  
                    $X \\rightarrow 45\\%$  
                \\end{tabular}  
            }  
        \\end{center}  
        \\begin{align\*}  
            X &= \\frac{45(132)}{100} \\\\  
            X &= \\frac{5940}{100} \\\\  
            X &= \\mathbf{59.4}  
        \\end{align\*}  
        \\item Si $8$ kg de manzanas cuestan $\\$450$ ¿cuánto comprar con $1700$?  
        \\begin{center}  
            \\fbox{  
                \\begin{tabular}{c}  
                    $8 \\text{ kg} \\rightarrow \\$450$ \\\\  
                    $X \\rightarrow \\$1700$  
                \\end{tabular}  
            }  
        \\end{center}  
        \\begin{align\*}  
            X &= \\frac{1700(8)}{450} \\\\  
            X &= \\frac{13600}{450} \\\\  
            X &= \\mathbf{30.22 \\text{ kg}}  
        \\end{align\*}  
        \\item $6$ jardineros podan el jardín en $3$ días. ¿Cuántos se requieren para $2$ días?  
        \\begin{center}  
            \\fbox{  
                \\begin{tabular}{c}  
                    $6 \\text{ jard.} \\rightarrow 3 \\text{ días}$ \\\\  
                    $X \\rightarrow 2 \\text{ días}$  
                \\end{tabular}  
            }  
        \\end{center}  
        \\begin{align\*}  
            X &= \\frac{6(3)}{2} \\\\  
            X &= \\frac{18}{2} \\\\  
            X &= \\mathbf{9 \\text{ jard.}}  
        \\end{align\*}  
        \\item Una bocina costaba $\\$1300$. Si descontaron $\\$300$ ¿cuál fue el porcentaje del descuento?  
        \\begin{center}  
            \\fbox{  
                \\begin{tabular}{c}  
                    $100\\% \\rightarrow \\$1300$ \\\\  
                    $X \\rightarrow \\$300$  
                \\end{tabular}  
            }  
        \\end{center}  
        \\begin{align\*}  
            X &= \\frac{300(100)}{1300} \\\\  
            X &= \\frac{30000}{1300} \\\\  
            X &= \\mathbf{23.07\\%}  
        \\end{align\*}  
    \\end{itemize}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 4}\\end{center}  
    \\begin{itemize}\[label={}, leftmargin=0pt\]  
        \\item Calcula el $36\\%$ de $520$.  
        \\begin{center}  
            \\fbox{  
                \\begin{tabular}{c}  
                    $520 \\rightarrow 100\\%$ \\\\  
                    $X \\rightarrow 36\\%$  
                \\end{tabular}  
            }  
        \\end{center}  
        \\begin{align\*}  
            X &= \\frac{36(520)}{100} \\\\  
            X &= \\frac{18720}{100} \\\\  
            X &= \\mathbf{187.2}  
        \\end{align\*}  
        \\item Si $4$ kg de fresas cuestan $\\$190$ ¿cuánto comprar con $300$?  
        \\begin{center}  
            \\fbox{  
                \\begin{tabular}{c}  
                    $4 \\text{ kg} \\rightarrow \\$190$ \\\\  
                    $X \\rightarrow \\$300$  
                \\end{tabular}  
            }  
        \\end{center}  
        \\begin{align\*}  
            X &= \\frac{300(4)}{190} \\\\  
            X &= \\frac{1200}{190} \\\\  
            X &= \\mathbf{6.31 \\text{ kg}}  
        \\end{align\*}  
        \\item $5$ trabajadores pintan en $3$ días. ¿Cuántos se requieren para $1$ día?  
        \\begin{center}  
            \\fbox{  
                \\begin{tabular}{c}  
                    $5 \\text{ trab.} \\rightarrow 3 \\text{ días}$ \\\\  
                    $X \\rightarrow 1 \\text{ día}$  
                \\end{tabular}  
            }  
        \\end{center}  
        \\begin{align\*}  
            X &= \\frac{5(3)}{1} \\\\  
            X &= \\frac{15}{1} \\\\  
            X &= \\mathbf{15 \\text{ trab.}}  
        \\end{align\*}  
        \\item Un pantalón costaba $\\$620$. Si descontaron $\\$300$ ¿cuál fue el porcentaje del descuento?  
        \\begin{center}  
            \\fbox{  
                \\begin{tabular}{c}  
                    $100\\% \\rightarrow \\$620$ \\\\  
                    $X \\rightarrow \\$300$  
                \\end{tabular}  
            }  
        \\end{center}  
        \\begin{align\*}  
            X &= \\frac{300(100)}{620} \\\\  
            X &= \\frac{30000}{620} \\\\  
            X &= \\mathbf{48.38\\%}  
        \\end{align\*}  
    \\end{itemize}  
\\end{minipage}  
% \--- FIN\_SECCION: RESOLUCIONES \---

\\newpage

% \--- INICIO\_SECCION: EXTRAS \---  
\\section\*{\\centering Ejercicios Extras}

\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 1}\\end{center}  
    \\begin{itemize}\[label={}, leftmargin=0pt, itemsep=1.5em\]  
        \\item Calcula el $25\\%$ de $840$.  
        \\item Si $12$ kg de azúcar cuestan $\\$180$ ¿cuánto comprar con $\\$500$?  
        \\item $8$ obreros construyen una barda en $15$ días. ¿Cuánto tardarán $12$ obreros?  
        \\item Un artículo cuesta $\\$2400$. Si tiene un $20\\%$ de descuento, ¿cuánto se debe pagar?  
    \\end{itemize}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 2}\\end{center}  
    \\begin{itemize}\[label={}, leftmargin=0pt, itemsep=1.5em\]  
        \\item Calcula el $5\\%$ de $2400$.  
        \\item Una televisión costaba $\\$8500$. Si descontaron $\\$1200$ ¿qué porcentaje descontaron?  
        \\item $6$ grifos llenan una alberca en $4$ horas. ¿Cuánto tardarán $10$ grifos?  
        \\item Si con $15$ litros de gasolina se recorren $180$ km, ¿cuántos km se recorren con $40$ litros?  
    \\end{itemize}  
\\end{minipage}

\\vspace{2em}

\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 3}\\end{center}  
    \\begin{itemize}\[label={}, leftmargin=0pt, itemsep=1.5em\]  
        \\item Calcula el $150\\%$ de $80$.  
        \\item Si $5$ metros de tela cuestan $\\$320$ ¿cuánto comprar con $\\$1000$?  
        \\item $3$ bombas de agua vacían un depósito en $8$ horas. ¿Cuántas bombas se necesitan para vaciarlo en $2$ horas?  
        \\item Un auto viaja a $80$ km/h y tarda $3$ horas. ¿Cuánto tardará si viaja a $120$ km/h?  
    \\end{itemize}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 4}\\end{center}  
    \\begin{itemize}\[label={}, leftmargin=0pt, itemsep=1.5em\]  
        \\item Una laptop costaba $\\$12000$. Si tiene el $15\\%$ de descuento ¿cuánto dinero se descontó?  
        \\item Si un auto recorre $450$ km con $30$ litros ¿cuántos litros necesita para $1200$ km?  
        \\item $10$ impresoras terminan un trabajo en $30$ minutos. ¿Cuánto tardarán $25$ impresoras?  
        \\item Calcula el $8.5\\%$ de $1500$.  
    \\end{itemize}  
\\end{minipage}  
% \--- FIN\_SECCION: EXTRAS \---

\\end{document}

# 13 problemas con fracciones

# 14 matematica griega

\\documentclass\[11pt\]{article}  
\\usepackage\[margin=1.5cm\]{geometry}  
\\usepackage{fontspec}  
\\setmainfont{Noto Sans}  
\\usepackage{amsmath, amssymb}  
\\usepackage{enumitem}  
\\usepackage{tikz}  
\\pagestyle{empty}

% Configuración para listas de ejercicios  
\\setlist\[itemize\]{label={}, leftmargin=0pt, itemsep=1.5em}

\\begin{document}

% \--- INICIO\_SECCION: TITULO \---  
\\begin{center}  
    {\\Huge \\textbf{Operaciones con Fracciones}}  
\\end{center}  
\\hrule  
\\vspace{1em}  
% \--- FIN\_SECCION: TITULO \---

% \--- INICIO\_SECCION: APUNTE \---  
\\section\*{\\centering Mini Apunte}

Todas las fracciones se tienen que simplificar al menos: mitades, terceras y quintas.

\\begin{itemize}  
    \\item \\textbf{Sumas y restas:} $\\dfrac{a}{b} \\pm \\dfrac{c}{d} \= \\dfrac{ad \\pm cb}{bd}$  
    \\item \\textbf{Multiplicación:} $\\dfrac{a}{b} \\left( \\dfrac{c}{d} \\right) \= \\dfrac{ac}{bd}$  
    \\item \\textbf{División:} $\\dfrac{a}{b} \\div \\dfrac{c}{d} \= \\dfrac{ad}{bc}$ \\quad ó \\quad $\\dfrac{\\frac{a}{b}}{\\frac{c}{d}} \= \\dfrac{ad}{bc}$  
    \\item \\textbf{Potencia:} $\\left( \\dfrac{a}{b} \\right)^n \= \\dfrac{a^n}{b^n}$  
    \\item \\textbf{Raíces:} $\\sqrt\[n\]{\\dfrac{a}{b}} \= \\dfrac{\\sqrt\[n\]{a}}{\\sqrt\[n\]{b}}$  
\\end{itemize}  
\\vspace{1em}  
\\rule{\\textwidth}{0.4pt}  
% \--- FIN\_SECCION: APUNTE \---

% \--- INICIO\_SECCION: EJEMPLOS \---  
\\section\*{\\centering Ejemplos}

\\begin{itemize}  
    \\item \\textbf{Suma y resta:} $-\\dfrac{3}{4} \- \\dfrac{8}{6} \= \\dfrac{-18 \- 32}{24} \= \\dfrac{-50}{24} \= \\mathbf{-\\dfrac{25}{12}}$  
    \\item \\textbf{Multiplicación:} $-\\dfrac{5}{8} \\left( \\dfrac{1}{2} \\right) \\left( \\dfrac{4}{10} \\right) \= \\dfrac{-20}{160} \= \\dfrac{-10}{80} \= \\mathbf{-\\dfrac{1}{8}}$  
    \\item \\textbf{División:} $\\dfrac{3}{4} \\div \\dfrac{8}{12} \= \\dfrac{36}{32} \= \\dfrac{18}{16} \= \\mathbf{\\dfrac{9}{8}}$ \\quad ó \\quad $\\dfrac{\\frac{3}{4}}{\\frac{8}{12}} \= \\dfrac{36}{32} \= \\mathbf{\\dfrac{9}{8}}$  
    \\item \\textbf{Potencia:} $\\left( \\dfrac{5}{-3} \\right)^3 \= \\dfrac{(5)^3}{(-3)^3} \= \\mathbf{\\dfrac{125}{-27}}$  
    \\item \\textbf{Raíces:} $\\sqrt{\\dfrac{36}{25}} \= \\dfrac{\\sqrt{36}}{\\sqrt{25}} \= \\mathbf{\\dfrac{6}{5}}$  
\\end{itemize}  
\\vspace{1em}  
\\rule{\\textwidth}{0.4pt}  
% \--- FIN\_SECCION: EJEMPLOS \---

\\newpage

% \--- INICIO\_SECCION: EJERCICIOS \---  
\\section\*{\\centering Ejercicios}

\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 1}\\end{center}  
    \\begin{itemize}  
        \\item $-\\dfrac{4}{8} \+ \\dfrac{1}{4} \=$  
        \\item $\\dfrac{4}{3} \\left( \\dfrac{5}{15} \\right) \=$  
        \\item $\\dfrac{3}{4} \\div \\dfrac{-2}{6} \=$  
        \\item $\\left( \\dfrac{2}{5} \\right)^2 \=$  
        \\item $\\sqrt{\\dfrac{25}{36}} \=$  
        \\item $-\\dfrac{2}{4} \- \\dfrac{5}{3} \=$  
        \\item $\\dfrac{2}{4} \\left( \\dfrac{7}{14} \\right) \\left( \\dfrac{-1}{3} \\right) \=$  
        \\item $\\dfrac{-\\frac{1}{2}}{-\\frac{4}{6}} \=$  
        \\item $\\left( \\dfrac{1}{-5} \\right)^3 \=$  
        \\item $\\sqrt\[3\]{\\dfrac{-8}{1000}} \=$  
    \\end{itemize}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 2}\\end{center}  
    \\begin{itemize}  
        \\item $\\dfrac{3}{6} \- \\dfrac{2}{5} \=$  
        \\item $-\\dfrac{1}{3} \\left( \-\\dfrac{2}{4} \\right) \=$  
        \\item $-\\dfrac{1}{2} \\div \\dfrac{5}{3} \=$  
        \\item $\\left( \\dfrac{-1}{4} \\right)^2 \=$  
        \\item $\\sqrt{\\dfrac{49}{4}} \=$  
        \\item $-\\dfrac{3}{5} \- \\dfrac{2}{10} \=$  
        \\item $-\\dfrac{3}{9} \\left( \\dfrac{4}{5} \\right) \\left( \\dfrac{1}{3} \\right) \=$  
        \\item $\\dfrac{-\\frac{2}{5}}{-\\frac{4}{3}} \=$  
        \\item $\\left( \-\\dfrac{2}{5} \\right)^3 \=$  
        \\item $\\sqrt\[3\]{\\dfrac{-64}{125}} \=$  
    \\end{itemize}  
\\end{minipage}

\\vspace{3em}

\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 3}\\end{center}  
    \\begin{itemize}  
        \\item $-\\dfrac{3}{5} \- \\dfrac{2}{4} \=$  
        \\item $-\\dfrac{2}{5} \\left( \-\\dfrac{4}{6} \\right) \=$  
        \\item $-\\dfrac{2}{3} \\div \\dfrac{1}{4} \=$  
        \\item $\\left( \-\\dfrac{1}{3} \\right)^2 \=$  
        \\item $\\sqrt{\\dfrac{81}{49}} \=$  
        \\item $\\dfrac{7}{10} \- \\dfrac{6}{10} \=$  
        \\item $-\\dfrac{2}{3} \\left( \-\\dfrac{9}{6} \\right) \\left( \\dfrac{-1}{3} \\right) \=$  
        \\item $\\dfrac{-\\frac{1}{3}}{\\frac{2}{6}} \=$  
        \\item $\\left( \\dfrac{4}{6} \\right)^3 \=$  
        \\item $\\sqrt\[3\]{\\dfrac{-1}{8}} \=$  
    \\end{itemize}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 4}\\end{center}  
    \\begin{itemize}  
        \\item $-\\dfrac{2}{8} \+ \\dfrac{6}{9} \=$  
        \\item $-\\dfrac{6}{3} \\left( \\dfrac{5}{20} \\right) \=$  
        \\item $\\dfrac{-6}{4} \\div \\dfrac{3}{-5} \=$  
        \\item $\\left( \-\\dfrac{2}{4} \\right)^2 \=$  
        \\item $\\sqrt{\\dfrac{4}{49}} \=$  
        \\item $-\\dfrac{4}{5} \- \\dfrac{6}{9} \=$  
        \\item $\\dfrac{4}{8} \\left( \\dfrac{1}{4} \\right) \\left( \\dfrac{-3}{2} \\right) \=$  
        \\item $\\dfrac{\\frac{2}{3}}{-\\frac{5}{4}} \=$  
        \\item $\\left( \-\\dfrac{3}{5} \\right)^3 \=$  
        \\item $\\sqrt\[3\]{\\dfrac{-125}{1000}} \=$  
    \\end{itemize}  
\\end{minipage}  
\\vspace{1em}  
\\rule{\\textwidth}{0.4pt}  
% \--- FIN\_SECCION: EJERCICIOS \---

\\newpage

% \--- INICIO\_SECCION: RESOLUCIONES \---  
\\section\*{\\centering Resoluciones}

\\begin{minipage}\[t\]{0.48\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 1}\\end{center}  
    \\begin{itemize}  
        \\item $-\\dfrac{4}{8} \+ \\dfrac{1}{4} \= \\dfrac{-16+8}{32} \= \\dfrac{-8}{32} \= \\mathbf{-\\dfrac{1}{4}}$  
        \\item $\\dfrac{4}{3} \\left( \\dfrac{5}{15} \\right) \= \\dfrac{20}{45} \= \\mathbf{\\dfrac{4}{9}}$  
        \\item $\\dfrac{3}{4} \\div \\dfrac{-2}{6} \= \\dfrac{18}{-8} \= \\mathbf{-\\dfrac{9}{4}}$  
        \\item $\\left( \\dfrac{2}{5} \\right)^2 \= \\dfrac{(2)^2}{(5)^2} \= \\mathbf{\\dfrac{4}{25}}$  
        \\item $\\sqrt{\\dfrac{25}{36}} \= \\dfrac{\\sqrt{25}}{\\sqrt{36}} \= \\mathbf{\\dfrac{5}{6}}$  
        \\item $-\\dfrac{2}{4} \- \\dfrac{5}{3} \= \\dfrac{-6-20}{12} \= \\dfrac{-26}{12} \= \\mathbf{-\\dfrac{13}{6}}$  
        \\item $\\dfrac{2}{4} \\left( \\dfrac{7}{14} \\right) \\left( \\dfrac{-1}{3} \\right) \= \\dfrac{-14}{168} \= \\mathbf{-\\dfrac{1}{12}}$  
        \\item $\\dfrac{-\\frac{1}{2}}{-\\frac{4}{6}} \= \\dfrac{-6}{-8} \= \\mathbf{\\dfrac{3}{4}}$  
        \\item $\\left( \\dfrac{1}{-5} \\right)^3 \= \\dfrac{(1)^3}{(-5)^3} \= \\mathbf{-\\dfrac{1}{125}}$  
        \\item $\\sqrt\[3\]{\\dfrac{-8}{1000}} \= \\dfrac{\\sqrt\[3\]{-8}}{\\sqrt\[3\]{1000}} \= \\mathbf{-\\dfrac{2}{10}}$  
    \\end{itemize}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.48\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 2}\\end{center}  
    \\begin{itemize}  
        \\item $\\dfrac{3}{6} \- \\dfrac{2}{5} \= \\dfrac{15-12}{30} \= \\dfrac{3}{30} \= \\mathbf{\\dfrac{1}{10}}$  
        \\item $-\\dfrac{1}{3} \\left( \-\\dfrac{2}{4} \\right) \= \\dfrac{2}{12} \= \\mathbf{\\dfrac{1}{6}}$  
        \\item $-\\dfrac{1}{2} \\div \\dfrac{5}{3} \= \\mathbf{-\\dfrac{3}{10}}$  
        \\item $\\left( \-\\dfrac{1}{4} \\right)^2 \= \\dfrac{(-1)^2}{(4)^2} \= \\mathbf{\\dfrac{1}{16}}$  
        \\item $\\sqrt{\\dfrac{49}{4}} \= \\dfrac{\\sqrt{49}}{\\sqrt{4}} \= \\mathbf{\\dfrac{7}{2}}$  
        \\item $-\\dfrac{3}{5} \- \\dfrac{2}{10} \= \\dfrac{-30-10}{50} \= \\dfrac{-40}{50} \= \\mathbf{-\\dfrac{4}{5}}$  
        \\item $-\\dfrac{3}{9} \\left( \\dfrac{4}{5} \\right) \\left( \\dfrac{1}{3} \\right) \= \\dfrac{-12}{135} \= \\mathbf{-\\dfrac{4}{45}}$  
        \\item $\\dfrac{-\\frac{2}{5}}{-\\frac{4}{3}} \= \\dfrac{-6}{-20} \= \\mathbf{\\dfrac{3}{10}}$  
        \\item $\\left( \-\\dfrac{2}{5} \\right)^3 \= \\dfrac{(-2)^3}{(5)^3} \= \\mathbf{-\\dfrac{8}{125}}$  
        \\item $\\sqrt\[3\]{\\dfrac{-64}{125}} \= \\dfrac{\\sqrt\[3\]{-64}}{\\sqrt\[3\]{125}} \= \\mathbf{-\\dfrac{4}{5}}$  
    \\end{itemize}  
\\end{minipage}

\\newpage

\\begin{minipage}\[t\]{0.48\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 3}\\end{center}  
    \\begin{itemize}  
        \\item $-\\dfrac{3}{5} \- \\dfrac{2}{4} \= \\dfrac{-12-10}{20} \= \\dfrac{-22}{20} \= \\mathbf{-\\dfrac{11}{10}}$  
        \\item $-\\dfrac{2}{5} \\left( \-\\dfrac{4}{6} \\right) \= \\dfrac{8}{30} \= \\mathbf{\\dfrac{4}{15}}$  
        \\item $-\\dfrac{2}{3} \\div \\dfrac{1}{4} \= \\mathbf{-\\dfrac{8}{3}}$  
        \\item $\\left( \-\\dfrac{1}{3} \\right)^2 \= \\dfrac{(-1)^2}{(3)^2} \= \\mathbf{\\dfrac{1}{9}}$  
        \\item $\\sqrt{\\dfrac{81}{49}} \= \\dfrac{\\sqrt{81}}{\\sqrt{49}} \= \\mathbf{\\dfrac{9}{7}}$  
        \\item $\\dfrac{7}{10} \- \\dfrac{6}{10} \= \\dfrac{70-60}{100} \= \\dfrac{10}{100} \= \\mathbf{\\dfrac{1}{10}}$  
        \\item $-\\dfrac{2}{3} \\left( \-\\dfrac{9}{6} \\right) \\left( \\dfrac{-1}{3} \\right) \= \\dfrac{-18}{54} \= \\mathbf{-\\dfrac{1}{3}}$  
        \\item $\\dfrac{-\\frac{1}{3}}{\\frac{2}{6}} \= \\dfrac{-6}{6} \= \\mathbf{-1}$  
        \\item $\\left( \\dfrac{4}{6} \\right)^3 \= \\dfrac{(4)^3}{(6)^3} \= \\dfrac{64}{216} \= \\mathbf{\\dfrac{8}{27}}$  
        \\item $\\sqrt\[3\]{\\dfrac{-1}{8}} \= \\dfrac{\\sqrt\[3\]{-1}}{\\sqrt\[3\]{8}} \= \\mathbf{-\\dfrac{1}{2}}$  
    \\end{itemize}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.48\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 4}\\end{center}  
    \\begin{itemize}  
        \\item $-\\dfrac{2}{8} \+ \\dfrac{6}{9} \= \\dfrac{-18+48}{72} \= \\dfrac{30}{72} \= \\mathbf{\\dfrac{5}{12}}$  
        \\item $-\\dfrac{6}{3} \\left( \\dfrac{5}{20} \\right) \= \\dfrac{-30}{60} \= \\mathbf{-\\dfrac{1}{2}}$  
        \\item $\\dfrac{-6}{4} \\div \\dfrac{3}{-5} \= \\dfrac{30}{12} \= \\mathbf{\\dfrac{15}{6} \= \\dfrac{5}{2}}$  
        \\item $\\left( \-\\dfrac{2}{4} \\right)^2 \= \\dfrac{(-2)^2}{(4)^2} \= \\dfrac{4}{16} \= \\mathbf{\\dfrac{1}{4}}$  
        \\item $\\sqrt{\\dfrac{4}{49}} \= \\dfrac{\\sqrt{4}}{\\sqrt{49}} \= \\mathbf{\\dfrac{2}{7}}$  
        \\item $-\\dfrac{4}{5} \- \\dfrac{6}{9} \= \\dfrac{-36-30}{45} \= \\dfrac{-66}{45} \= \\mathbf{-\\dfrac{22}{15}}$  
        \\item $\\dfrac{4}{8} \\left( \\dfrac{1}{4} \\right) \\left( \\dfrac{-3}{2} \\right) \= \\dfrac{-12}{64} \= \\mathbf{-\\dfrac{3}{16}}$  
        \\item $\\dfrac{\\frac{2}{3}}{-\\frac{5}{4}} \= \\mathbf{-\\dfrac{8}{15}}$  
        \\item $\\left( \-\\dfrac{3}{5} \\right)^3 \= \\dfrac{(-3)^3}{(5)^3} \= \\mathbf{-\\dfrac{27}{125}}$  
        \\item $\\sqrt\[3\]{\\dfrac{-125}{1000}} \= \\dfrac{\\sqrt\[3\]{-125}}{\\sqrt\[3\]{1000}} \= \\mathbf{-\\dfrac{5}{10} \= \-\\dfrac{1}{2}}$  
    \\end{itemize}  
\\end{minipage}  
\\vspace{1em}  
\\rule{\\textwidth}{0.4pt}  
% \--- FIN\_SECCION: RESOLUCIONES \---

\\newpage

% \--- INICIO\_SECCION: EXTRAS \---  
\\section\*{\\centering Ejercicios Extras}

\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 5}\\end{center}  
    \\begin{itemize}  
        \\item $-\\dfrac{7}{14} \+ \\dfrac{3}{7} \=$  
        \\item $-\\dfrac{5}{10} \- \\dfrac{3}{4} \=$  
        \\item $\\dfrac{6}{5} \\left( \\dfrac{7}{25} \\right) \=$  
        \\item $\\dfrac{4}{9} \\left( \\dfrac{5}{15} \\right) \\left( \-\\dfrac{3}{8} \\right) \=$  
        \\item $\\dfrac{3}{5} \\div \-\\dfrac{5}{8} \=$  
        \\item $-\\dfrac{4}{7} \\div \-\\dfrac{6}{9} \=$  
        \\item $\\left( \\dfrac{2}{3} \\right)^2 \=$  
        \\item $\\left( \-\\dfrac{3}{8} \\right)^3 \=$  
        \\item $\\sqrt{\\dfrac{49}{81}} \=$  
        \\item $\\sqrt\[3\]{-\\dfrac{64}{125}} \=$  
    \\end{itemize}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 6}\\end{center}  
    \\begin{itemize}  
        \\item $-\\dfrac{8}{16} \+ \\dfrac{5}{10} \=$  
        \\item $-\\dfrac{2}{5} \- \\dfrac{4}{7} \=$  
        \\item $\\dfrac{5}{6} \\left( \\dfrac{8}{24} \\right) \=$  
        \\item $\\dfrac{7}{9} \\left( \\dfrac{3}{12} \\right) \\left( \-\\dfrac{4}{5} \\right) \=$  
        \\item $\\dfrac{3}{4} \\div \-\\dfrac{7}{10} \=$  
        \\item $-\\dfrac{5}{6} \\div \-\\dfrac{7}{8} \=$  
        \\item $\\left( \\dfrac{5}{8} \\right)^2 \=$  
        \\item $\\left( \-\\dfrac{4}{9} \\right)^3 \=$  
        \\item $\\sqrt{\\dfrac{16}{49}} \=$  
        \\item $\\sqrt\[3\]{-\\dfrac{27}{64}} \=$  
    \\end{itemize}  
\\end{minipage}

\\vspace{3em}

\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 7}\\end{center}  
    \\begin{itemize}  
        \\item $-\\dfrac{9}{18} \+ \\dfrac{4}{9} \=$  
        \\item $-\\dfrac{7}{14} \- \\dfrac{2}{5} \=$  
        \\item $\\dfrac{3}{7} \\left( \\dfrac{4}{21} \\right) \=$  
        \\item $\\dfrac{5}{11} \\left( \\dfrac{2}{14} \\right) \\left( \-\\dfrac{5}{9} \\right) \=$  
        \\item $\\dfrac{5}{6} \\div \-\\dfrac{3}{4} \=$  
        \\item $-\\dfrac{2}{3} \\div \-\\dfrac{5}{8} \=$  
        \\item $\\left( \\dfrac{4}{9} \\right)^2 \=$  
        \\item $\\left( \-\\dfrac{5}{8} \\right)^3 \=$  
        \\item $\\sqrt{\\dfrac{36}{49}} \=$  
        \\item $\\sqrt\[3\]{-\\dfrac{125}{216}} \=$  
    \\end{itemize}  
\\end{minipage}  
\\hfill  
\\begin{minipage}\[t\]{0.45\\textwidth}  
    \\begin{center}\\textbf{\\large Bloque 8}\\end{center}  
    \\begin{itemize}  
        \\item $-\\dfrac{5}{12} \+ \\dfrac{3}{8} \=$  
        \\item $-\\dfrac{3}{7} \- \\dfrac{1}{4} \=$  
        \\item $\\dfrac{8}{9} \\left( \\dfrac{5}{27} \\right) \=$  
        \\item $\\dfrac{4}{7} \\left( \\dfrac{6}{20} \\right) \\left( \-\\dfrac{3}{5} \\right) \=$  
        \\item $\\dfrac{7}{10} \\div \-\\dfrac{2}{5} \=$  
        \\item $-\\dfrac{4}{9} \\div \-\\dfrac{3}{7} \=$  
        \\item $\\left( \\dfrac{3}{8} \\right)^2 \=$  
        \\item $\\left( \-\\dfrac{4}{11} \\right)^3 \=$  
        \\item $\\sqrt{\\dfrac{25}{64}} \=$  
        \\item $\\sqrt\[3\]{-\\dfrac{8}{27}} \=$  
    \\end{itemize}  
\\end{minipage}

\\vspace{1em}  
\\rule{\\textwidth}{0.4pt}  
% \--- FIN\_SECCION: EXTRAS \---

\\end{document}  

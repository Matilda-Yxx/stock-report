The "porty" directory is a Python package of code. This package is inspired by the [course](https://dabeaz-course.github.io/practical-python/Notes/Contents.html) taught by the python guru David Beazley.  

The "print-report.py" program is a top-level script that
produces a report based on a list of stock prices and a given portofolio. Try it!

```
shell % python3 print-report.py portfolio.csv prices.csv txt
      Name     Shares      Price     Change 
---------- ---------- ---------- ---------- 
        AA        100       9.22     -22.98 
       IBM         50     106.28      15.18 
       CAT        150      35.46     -47.98 
      MSFT        200      20.89     -30.34 
        GE         95      13.48     -26.89 
      MSFT         50      20.89     -44.21 
       IBM        100     106.28      35.84 
shell %
```

Other than the txt format, you can also display the portfolio in csv or html 
formats.

HTML:
```html
<tr><th>Name</th><th>Shares</th><th>Price</th><th>Change</th></tr>
<tr><td>AA</td><td>100</td><td>9.22</td><td>-22.98</td></tr>
<tr><td>IBM</td><td>50</td><td>106.28</td><td>15.18</td></tr>
<tr><td>CAT</td><td>150</td><td>35.46</td><td>-47.98</td></tr>
<tr><td>MSFT</td><td>200</td><td>20.89</td><td>-30.34</td></tr>
<tr><td>GE</td><td>95</td><td>13.48</td><td>-26.89</td></tr>
<tr><td>MSFT</td><td>50</td><td>20.89</td><td>-44.21</td></tr>
<tr><td>IBM</td><td>100</td><td>106.28</td><td>35.84</td></tr>
```

This is one of the first python apps that I've written on my own. I learned much
through this project, be it generators, mixin pattern, decorators, etc. In case you're interested, I have also published my course notes in this repo.

David's course progressed from very basic to more advanced topics. I already had some python experience before taking this course (but my experience was largely restricted to data science projects), so I still find this course quite useful! If you're into python's wonderful features, I'd greatly recommend the book Luciano Ramalho's *Fluent Python* as a continuation from David's course.

Happy learning!
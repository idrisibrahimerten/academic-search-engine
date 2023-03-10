<img align="left" width="250" height="250" src="academic_search_engine_logo.png"> <br>

<br>



# Academic Search Engine
<br>


<br>


<br>

## Description
* Our project was developed on the basis of determining the sites frequently used by the academicians, and outputting the links of the article studies according to the input that they search automatically through the sites. <br>
Our project works with search engine logic. You enter the topic you are looking for in the search engine and you will get results. This study also works only on academic research. Simply enter the topic you are looking for and define how many articles you want. <br>
Project workspace platforms are as follows; <br>
  * Google Akademik
  * Dergi Park 
  * Science Direct
 <br>
! We are waiting for your development support to work on more platforms. <br>

## How to Setup?
* We have made it work in the PYPI environment, which allows you to automatically install our project, so you can install it automatically using the following command.
```shell
pip install academic-search-engine
```
---
## How to RUN?
* To run our project, it is sufficient to examine the content of the example file.

## Project Test
```
from academic_search_engine import academic_search_engine

result = academic_search_engine()


"""
Returns Dergipark and Google Scholar results.
"""
result.sayfa("big data", 1)
```

* Result:
```json
{
   "Dergi Park Link": "https://dergipark.org.tr/tr/pub/connectist/issue/56249/775841",
   "Google Akademik Link": "https://www.nature.com/articles/498255a"
}
```

```json
[{'Dergi Park Link': 'https://dergipark.org.tr/tr/pub/connectist/issue/56249/775841', 'Google Akademik Link': 'https://www.nature.com/articles/498255a'}, {'Dergi Park Link': 'https://dergipark.org.tr/tr/pub/iktisad/issue/72676/1144242', 'Google Akademik Link': 'http://dbjournal.ro/archive/10/10.pdf'}, {'Dergi Park Link': 'https://dergipark.org.tr/tr/pub/ajit-e/issue/54422/740748', 'Google Akademik Link': 'https://iacis.org/iis/2015/2_iis_2015_81-90.pdf'}, {'Dergi Park Link': 'https://dergipark.org.tr/tr/pub/jes/issue/64868/878318', 'Google Akademik Link': 'https://citeseerx.ist.psu.edu/document?repid=rep1&amp;type=pdf&amp;doi=2d562bb0dbb0c5b757be86995f5497e760c769b8'}, {'Dergi Park Link': 'https://dergipark.org.tr/tr/pub/iuchkd/issue/57846/813328', 'Google Akademik Link': 'https://rss.onlinelibrary.wiley.com/doi/pdf/10.1111/j.1740-9713.2014.00778.x'}, {'Dergi Park Link': 'https://dergipark.org.tr/tr/pub/ibad/issue/58423/827546', 'Google Akademik Link': 'https://ieeexplore.ieee.org/iel5/4236/6188571/06188576.pdf'}, {'Dergi Park Link': 'https://dergipark.org.tr/tr/pub/ejosat/issue/59648/822219', 'Google Akademik Link': 'https://books.google.com/books?hl=tr&amp;lr=&amp;id=p7d1BwAAQBAJ&amp;oi=fnd&amp;pg=PR8&amp;dq=big+data&amp;ots=72g6pMcWLr&amp;sig=M819r5jeynPW-zFaj-Mv-JbdGRg'}, {'Dergi Park Link': 'https://dergipark.org.tr/tr/pub/talid/issue/70969/1115782', 'Google Akademik Link': 'http://www.scielo.org.co/scielo.php?script=sci_arttext&amp;pid=S0121-11292015000100006'}, {'Dergi Park Link': 'https://dergipark.org.tr/tr/pub/trta/issue/60117/819385', 'Google Akademik Link': 'https://www.ias.ac.in/public/Volumes/reso/021/08/0695-0716.pdf'}, {'Dergi Park Link': 'https://dergipark.org.tr/tr/pub/dusuncevetoplum/issue/63163/915151', 'Google Akademik Link': 'https://ieeexplore.ieee.org/iel7/38/6562702/06562707.pdf'}]
```

## WARNINGS!

#### !Important Note!: In order to use the Science Direct platform, you must be registered to the platform and enter your user name and password into the program. Unless you take the program live or share it, no one can access your username and password, all responsibility belongs to the user.

#### !Important Note!: The project is not developed for web scraping and malicious purposes to collect data of people. The project was developed to bring all article "Platform Links" with a single input in order to minimize the time spent by academic research individuals researching on separate platforms. Responsibility belongs to the user. Do not use it for other than its intended purpose!

**************************************************************
#### T??rk??e 

## Tan??m
* Projemiz akademik ??al????ma yapan kimselerin s??k kulland??klar?? siteler belirlenerek siteler ??zerinden otomatik olarak arama yapt?????? girdiye g??re makale ??al????malar??n??n linklerini ????kt?? halinde getirmesi ??zerine geli??tirildi. <br>
Projemiz arama motoru mant?????? ile ??al????maktad??r. Arama motoruna arad??????n??z konuyu girersiniz ve sonu?? al??rs??n??z. Bu ??al????ma da sadece akademik ara??t??rmalar ??zerine ??al????maktad??r. Arad??????n?? konuyu girmeniz ve ka?? makale istedi??inizi tan??mlaman??z yeterlidir. <br>
Proje ??al????ma alan?? platformlar?? a??a????daki gibidir; <br>
  * Google Akademik
  * Dergi Park 
  * Science Direct
 <br>
! Daha fazla platformda ??al????mas?? i??in geli??tirme desteklerinizi bekliyoruz. <br>

## Nas??l Kurulur?
* Projemizi otomatik olarak kurman??za olanak sa??layan PYPI ortam??nda ??al????mas??n?? sa??lad??k bu sayede a??a????daki komutu kullanarak otomatik olarak kurabilirsiniz.
```shell
pip install academic-search-engine
```
---
## Nas??l ??al??????r?
* Projemizi ??al????t??rman??z i??in example dosyas?? i??erisini incelemeniz yeterlidir.

## Projeyi Test Edelim.
```
from academic_search_engine import academic_search_engine

result = academic_search_engine()


"""
Dergi Park ve Google Akademik sonu??lar??n?? d??nd??r??r.
"""
result.sayfa("big data", 1)
```

* Sonu??:
```json
{
   "Dergi Park Link": "https://dergipark.org.tr/tr/pub/connectist/issue/56249/775841",
   "Google Akademik Link": "https://www.nature.com/articles/498255a"
}
```

```json
[{'Dergi Park Link': 'https://dergipark.org.tr/tr/pub/connectist/issue/56249/775841', 'Google Akademik Link': 'https://www.nature.com/articles/498255a'}, {'Dergi Park Link': 'https://dergipark.org.tr/tr/pub/iktisad/issue/72676/1144242', 'Google Akademik Link': 'http://dbjournal.ro/archive/10/10.pdf'}, {'Dergi Park Link': 'https://dergipark.org.tr/tr/pub/ajit-e/issue/54422/740748', 'Google Akademik Link': 'https://iacis.org/iis/2015/2_iis_2015_81-90.pdf'}, {'Dergi Park Link': 'https://dergipark.org.tr/tr/pub/jes/issue/64868/878318', 'Google Akademik Link': 'https://citeseerx.ist.psu.edu/document?repid=rep1&amp;type=pdf&amp;doi=2d562bb0dbb0c5b757be86995f5497e760c769b8'}, {'Dergi Park Link': 'https://dergipark.org.tr/tr/pub/iuchkd/issue/57846/813328', 'Google Akademik Link': 'https://rss.onlinelibrary.wiley.com/doi/pdf/10.1111/j.1740-9713.2014.00778.x'}, {'Dergi Park Link': 'https://dergipark.org.tr/tr/pub/ibad/issue/58423/827546', 'Google Akademik Link': 'https://ieeexplore.ieee.org/iel5/4236/6188571/06188576.pdf'}, {'Dergi Park Link': 'https://dergipark.org.tr/tr/pub/ejosat/issue/59648/822219', 'Google Akademik Link': 'https://books.google.com/books?hl=tr&amp;lr=&amp;id=p7d1BwAAQBAJ&amp;oi=fnd&amp;pg=PR8&amp;dq=big+data&amp;ots=72g6pMcWLr&amp;sig=M819r5jeynPW-zFaj-Mv-JbdGRg'}, {'Dergi Park Link': 'https://dergipark.org.tr/tr/pub/talid/issue/70969/1115782', 'Google Akademik Link': 'http://www.scielo.org.co/scielo.php?script=sci_arttext&amp;pid=S0121-11292015000100006'}, {'Dergi Park Link': 'https://dergipark.org.tr/tr/pub/trta/issue/60117/819385', 'Google Akademik Link': 'https://www.ias.ac.in/public/Volumes/reso/021/08/0695-0716.pdf'}, {'Dergi Park Link': 'https://dergipark.org.tr/tr/pub/dusuncevetoplum/issue/63163/915151', 'Google Akademik Link': 'https://ieeexplore.ieee.org/iel7/38/6562702/06562707.pdf'}]
```

## UYARILAR!

#### !??nemli Not!: Science Direct platformunu kullanman??z i??in platforma kay??tl?? olman??z ve kullan??c?? ad??, ??ifrenizi programa girmeniz gerekmektedir. Program?? canl??ya almad??????n??z veya payla??mad??????n??z s??rece kullan??c?? ad?? ve ??ifrenize kimse eri??emez t??m sorumluluk kullan??c??ya aittir.

#### !??nemli Not!: Proje web scraping ile ki??ilerin verilerini toplamak ve k??t?? ama??l?? geli??tirilmemi??tir. Proje akademik ara??t??rma yapan bireylerin ayr?? ayr?? platformlarda ara??t??rma yaparak ge??irdi??i s??reyi en aza indirmek i??in tek girdiyle t??m makale "Platform Linklerini" getirmek ??zere geli??tirildi. Sorumluluk kullan??c??ya aittir. Amac?? d??????nda kullanmay??n??z!

## ??stek ve ??ikayetleriniz ????in Mail G??ndermenizi Rica Ederim.

## Please send an e-mail for your requests and complaints.

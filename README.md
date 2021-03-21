<h1>Тестовое задание Junior Developer in QA Veeam</h1>
<h2>Задача 2 </h2>

<p>Дан файл, содержащий имена файлов, алгоритм хэширования (один из MD5/SHA1/SHA256) и
соответствующие им хэш-суммы, вычисленные по соответствующему алгоритму и указанные в
файле через пробел. Напишите программу, читающую данный файл и проверяющую
целостность файлов.</p>
Пример<br>
Файл сумм:<br>
file_01.bin md5 aaeab83fcc93cd3ab003fa8bfd8d8906<br>
file_02.bin md5 6dc2d05c8374293fe20bc4c22c236e2e<br>
file_03.bin md5 6dc2d05c8374293fe20bc4c22c236e2e<br>
file_04.txt sha1 da39a3ee5e6b4b0d3255bfef95601890afd80709<br>
<hr>
Пример вызова:
<b>your program => path to the input file => path to the directory containing the files to check</b>
<br><br>
Формат вывода: <br>
file_01.bin OK<br>
file_02.bin FAIL<br>
file_03.bin NOT FOUND<br>
file_04.txt OK
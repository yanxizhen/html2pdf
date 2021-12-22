# coding: utf-8

import subprocess
import tenacity
import os
import glob
from pathlib import Path

'''
调用playwright pdf "htmlfilepath" "pdffilename" 将本地html文件转换为pdf
也可稍作修改,将htmlfilepath改为url,直接转换web服务器上的网页为pdf
'''

@tenacity.retry(wait=tenacity.wait_fixed(1))
def html2pdf(infile, outputfile):
    '''
    转换html文件为pdf, 存在load page timeout错误,故使用tenacity一直重试,直至成功输出
    :param infile: html全路径
    :param outputfile: 输出pdf全路径
    :return: 
    '''
    retrycnt = html2pdf.retry.statistics['attempt_number']
    print(f'attempt: {retrycnt}')
 
    result = subprocess.check_call(f'playwright pdf "{infile}" "{outputfile}"', shell=False)

    if result != 0:
        raise Exception


if __name__ == '__main__':

    # 使用glob模块快速遍历文件夹内所有html文件
    htmlpath = 'D:\\htmldir'
    p = Path(htmlpath)
    htmlcnt = 0
    

    html_list = []
    for file in p.rglob('*.html'):
        html_list.append(str(file))
        htmlcnt = htmlcnt + 1
    print(f'{htmlcnt} 个html')

    # 使用glob模块快速遍历文件夹内所有pdf文件名
    pdfpath = 'D:\\outputpdf'
    p1 = Path(pdfpath)
    pdfcnt = 0
    
    pdf_list = []
    for file in p1.rglob('*.pdf'):
        pdf_list.append(str(file.stem))
        pdfcnt = pdfcnt + 1
    print(f'{pdfcnt} 个pdf')

    # 循环html文件列表,开始转换
    for x in html_list:
        htmlfilename = x.split('.')[0].split('\\')[-1]
        if htmlfilename in pdf_list:
            print(f'已存在 {htmlfilename}.pdf,跳过')
            continue
            
        outputfile = str(f'{pdfpath}\\{htmlfilename}.pdf')
        print(f'开始输出: {x} -> {outputfile}')
        html2pdf(x, outputfile)

#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import csv

def parse_csv_perf():
    filename = "perf.csv"
    out_filename = "perf_out.csv"
    
    of = open(out_filename, 'w')
    fieldnames = ['time', 'cpu', 'mem_pss_total']
    writer = csv.DictWriter(of, fieldnames=fieldnames)
    writer.writeheader()
    
    csv_if = open(filename)
    reader = csv.DictReader(csv_if)
    
    for row in reader:
        print(row['time'],row['cpu'], row['mem_pss_total'])
        data = {'time':row['time'],'cpu':row['cpu'],'mem_pss_total':row['mem_pss_total']}
        writer.writerow(data)
        
    csv_if.close()
    of.close()

if __name__ == "__main__":
    with open('examples.csv') as csvfile:
        read_csv = csv.reader(csvfile, delimiter=',')
        dates = []
        colors = []
        for row in read_csv:
            print(row)
            color = row[3]
            date = row[0]
            dates.append(date)
            colors.append(color)
        print(dates)
        print(colors)
        
    with open('names.csv', 'w') as csvfile:
        fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
        writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
        writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
        
    with open('eggs.csv', 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
        spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
    parse_csv_perf()
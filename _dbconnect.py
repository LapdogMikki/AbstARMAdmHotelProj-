import sqlite3
import os
from sqlite3.dbapi2 import Error
from tkinter import messagebox as mb
def connectDB():
    try:
        cnct=sqlite3.connect("gst.db")
        return cnct
    except Error:
        print(Error)
def showtabbron():
    con=connectDB()
    crs=con.cursor()
    crs.execute("SELECT rooms.nmb_room,client.FIO,resrvd.date_chckin,resrvd.date_evict FROM rooms,client,resrvd WHERE client.id_klient=resrvd.id_client and rooms.id_room=resrvd.id_room")
    data=(row for row in crs.fetchall()) 
    con.close()
    return data   
def showtabkli():
    con=connectDB()
    crs=con.cursor()
    crs.execute("SELECT FIO,phone,grzhd,udostlich,seria,nomer,visa,visa_beg_dat,visa_end_date FROM client")
    data=(row for row in crs.fetchall()) 
    con.close()
    return data   
def showtabrms():
    con=connectDB()
    crs=con.cursor()
    crs.execute("SELECT rooms.nmb_room,type_room.t_room,type_room.price FROM rooms,type_room WHERE rooms.id_type_room=type_room.id_type")
    data=(row for row in crs.fetchall()) 
    con.close()
    return data 
def showtabtprms():
    con=connectDB()
    crs=con.cursor()
    crs.execute("SELECT t_room,kolvo_mest,price FROM type_room")
    data=(row for row in crs.fetchall()) 
    con.close()
    return data 
def showtabusl():
    con=connectDB()
    crs=con.cursor()
    crs.execute("SELECT name_usluga,ed_izm,price FROM uslugs")
    data=(row for row in crs.fetchall()) 
    con.close()
    return data 
def showtabokusl():
    con=connectDB()
    crs=con.cursor()
    crs.execute("SELECT uslugs.name_usluga,client.FIO,ispolz_uslug.kol_vo,ispolz_uslug.date_usg,ispolz_uslug.price FROM client,uslugs,ispolz_uslug WHERE client.id_klient=ispolz_uslug.id_client and uslugs.id_usluga=ispolz_uslug.id_usluga")
    data=(row for row in crs.fetchall()) 
    con.close()
    return data 
def cbx_selectklts():
    con=connectDB()
    crs=con.cursor()
    crs.execute("SELECT FIO FROM client")
    data=[]
    for row in crs.fetchall():
        data.append(row[0])
    con.close()
    return data
def cbx_selectnmrs():
    con=connectDB()
    crs=con.cursor()
    crs.execute("SELECT nmb_room FROM rooms")
    data=[]
    for row in crs.fetchall():
        data.append(row[0])
    con.close()
    return data
def cbx_selectuslgs():
    con=connectDB()
    crs=con.cursor()
    crs.execute("SELECT name_usluga FROM uslugs")
    data=[]   
    for row in crs.fetchall():
        data.append(row[0])
    con.close()
    return data
    
def delete_clnt(table):
    def del_cl():
        if table.selection():
            con=connectDB()
            crs=con.cursor()
            curItem = table.focus()
            contents =(table.item(curItem))
            selecteditem = contents['values']
            table.delete(curItem)
            crs.execute("DELETE FROM client WHERE 'phone'=%s"%selecteditem[1])
            con.commit()
            con.close()
            showtabkli()
        else:
            mb.showerror('Ошибка','Не выделена запись')
    return del_cl

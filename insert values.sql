insert into tb_category values(1,'Books');
insert into tb_category values(2,'Pens');
insert into tb_category values(3,'Notebooks');
insert into tb_category values(4,'Markers');
insert into tb_category values(5,'Desk Materials');


insert into tb_product values(1,1,'Programming 1','Jamshid','12-Feb-2015');
insert into tb_product values(2,1,'Serat Nabi(PBUH)','Hamza','12-Feb-2022');
insert into tb_product values(3,1,'Sukoon Khar','Obaidullah Hussam','19-oct-2024');
insert into tb_product values(4,1,'Sahih al-Bukhari','Imam Bukhari','1-aug-846');
insert into tb_product values(5,3,'blank notebook',null,null);
insert into tb_product values(6,3,'Liner notebook',null,null);
insert into tb_product values(7,3,'A4 notebook',null,null);
insert into tb_product values(8,3,'Sticky Notes',null,null);
insert into tb_product values(9,2,'Linc',null,null);
insert into tb_product values(10,2,'Paino',null,null);
insert into tb_product values(11,2,'Havsar',null,null);
insert into tb_product values(12,2,'Dollar',null,null);
insert into tb_product values(13,4,'Whiteboard Marker',null,null);
insert into tb_product values(14,4,'Hilighter',null,null);
insert into tb_product values(15,4,'Chalk',null,null);
insert into tb_product values(16,4,'Draw Marker',null,null);
insert into tb_product values(17,5,'Ruler',null,null);
insert into tb_product values(18,5,'Dester',null,null);
insert into tb_product values(19,5,'Scissors',null,null);
insert into tb_product values(20,5,'Stapler',null,null);
insert into tb_product values(21,5,'Glue',null,null);


insert into tb_stock values(1,'First_Stock','Arzan-Qemat');
insert into tb_stock values(2,'Second_Stock','Shar-e-naw');
insert into tb_stock values(3,'Third_Stock','Kart-e-naw');
insert into tb_stock values(4,'Fourth_Stock','Parwan 3');


insert into tb_customer values(1,'Omid','Arzan-Qemat');
insert into tb_customer values(2,'Khalid','Shah-Shaheed');
insert into tb_customer values(3,'Jamal','Maqoryan');
insert into tb_customer values(4,'Asif','Jada');


insert into tb_employees values(1,'Kamal','Manager');
insert into tb_employees values(2,'Feroz','Cashier');
insert into tb_employees values(3,'Mula','Stock Manager');
insert into tb_employees values(4,'Baba','Worker');

insert into tb_supplier values(1,'Modir Mustafa','Paktia-Kot',0776101886);
insert into tb_supplier values(2,'Easa Murtaza','Sarak-e-naw',0785653065);

insert into tb_purchase values(1,1,sysdate);
insert into tb_purchase values(2,1,sysdate);
insert into tb_purchase values(3,1,sysdate);
insert into tb_purchase values(4,1,sysdate);
insert into tb_purchase values(5,2,sysdate);
insert into tb_purchase values(6,2,sysdate);
insert into tb_purchase values(7,2,sysdate);
insert into tb_purchase values(8,2,sysdate);


insert into tb_purchasedetails values(1,1,1,1,50,200);
insert into tb_purchasedetails values(2,2,2,1,100,350);
insert into tb_purchasedetails values(3,3,7,1,100,30);
insert into tb_purchasedetails values(4,4,8,1,200,20);
insert into tb_purchasedetails values(5,5,9,1,300,4);
insert into tb_purchasedetails values(6,6,12,1,250,7);
insert into tb_purchasedetails values(7,7,17,1,50,10);
insert into tb_purchasedetails values(8,8,18,1,50,20);



insert into tb_sales values(1,1,sysdate);
insert into tb_sales values(2,2,sysdate);

insert into tb_saledetails values(10,1,1,1,5,400);
insert into tb_saledetails values(11,2,2,1,10,700);


insert into tb_payment values(1,1,1,sysdate,10000);
insert into tb_payment values(2,1,2,sysdate,30000);
insert into tb_payment values(3,1,3,sysdate,3000);
insert into tb_payment values(4,1,4,sysdate,4000);
insert into tb_payment values(5,2,5,sysdate,2000);
insert into tb_payment values(6,3,6,sysdate,1000);
insert into tb_payment values(7,2,7,sysdate,2000);
insert into tb_payment values(8,3,8,sysdate,4000);
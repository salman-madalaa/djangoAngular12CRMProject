import { Component, OnInit } from '@angular/core';
import { CustomerOrderService } from '../services/customer-order.service';

@Component({
  selector: 'app-all',
  templateUrl: './all.component.html',
  styleUrls: ['./all.component.css']
})
export class AllComponent implements OnInit {
  customerOrders: any;
  customers:any;
  edit: boolean = false;
  enableEditIndex = null;

  newCustomerOrder={
    // id :'',
    customerId:'',
    orderDate:'',
    contact_phone: '',
    orderTotal: '',
  }

  constructor(private _cusOrderSer:CustomerOrderService) { }

  ngOnInit(): void {
    this.GetAllCustomerOrders();
  }

  GetAllCustomerOrders(){
    this._cusOrderSer.getallCustomerOrders().subscribe((data: any) =>{
      this.customerOrders = data.CustomerOrders;
      this.customers = data.customers;
      if (this.customerOrders != null ){
        this.customerOrders.forEach((element:any) => {
          element['isEdit'] = false;
        });
      }
      console.log(data);
    });
  }

  update(ob:any){
    // this.newCustomerOrder.id = ob.id;
    this.newCustomerOrder.customerId = ob.customerId;
    this.newCustomerOrder.orderDate = ob.orderDate;
    this.newCustomerOrder.contact_phone = ob.contact_phone;
    this.newCustomerOrder.orderTotal = ob.orderTotal;
    ob.isEdit = true;   
  }

  cancel(customer:any) {
    
    customer.isEdit = false;
  
  }

  save(ob:any,id:number) {
    console.log(ob);
    this._cusOrderSer.update(ob,id).subscribe((data: any) =>{
      console.log(data);
      this.GetAllCustomerOrders();
    });
  }

  delete(id:number){
    this._cusOrderSer.delete(id).subscribe((data: any) =>{
      console.log(data);
      this.GetAllCustomerOrders();
    });
  }

}

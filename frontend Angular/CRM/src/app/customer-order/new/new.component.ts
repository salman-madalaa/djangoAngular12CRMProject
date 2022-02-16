import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { CustomerService } from 'src/app/customer/services/customer.service';
import { CustomerOrderService } from '../services/customer-order.service';

@Component({
  selector: 'app-new',
  templateUrl: './new.component.html',
  styleUrls: ['./new.component.css']
})
export class NewComponent implements OnInit {
  customers:any;
  customerOrder={
    customerId:'',
    orderDate:'',
    contact_phone: '',
    orderTotal: ''
  }

  constructor(private _cusOrderSer:CustomerOrderService,private _cusSer:CustomerService,private router:Router) { }

  ngOnInit(): void {
    this.getCustomers();
  }

  getCustomers() {
    this._cusSer.getallCustomers().subscribe((data)=>{
      this.customers = data.customers;
      console.log(data.customers)
    })
  }

  create(customer:any){
    console.log(customer);
    this._cusOrderSer.createCustomerOrder(customer).subscribe(data=>{
      console.log(data);
      this.router.navigateByUrl('/customerOrder/all');
    })
  }
  

}

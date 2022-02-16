import { Component, OnInit } from '@angular/core';
import { CustomerService } from '../services/customer.service';

@Component({
  selector: 'app-all',
  templateUrl: './all.component.html',
  styleUrls: ['./all.component.css']
})
export class AllComponent implements OnInit {
  customers: any;
  edit: boolean = false;
  enableEditIndex = null;

  newCustomer={
    name:'',
    type:'',
    phone: '',
    address: ''
  }

  constructor(private _cusSer:CustomerService) { }

  ngOnInit(): void {
    this.GetAllCustomers();
  }

  GetAllCustomers(){
    this._cusSer.getallCustomers().subscribe((data: any) =>{
      this.customers = data.customers;
      this.customers.forEach((element:any) => {
        element['isEdit'] = false;
      });
      console.log(data);
    });
  }

  update(ob:any){
    this.newCustomer.name = ob.name;
    this.newCustomer.type = ob.type;
    this.newCustomer.phone = ob.phone;
    this.newCustomer.address = ob.address;
    ob.isEdit = true;   
  }

  cancel(customer:any){
    customer.isEdit = false;
  }

  save(ob:any,id:number){
    this._cusSer.update(ob,id).subscribe((data: any) =>{
      console.log(data);
      this.GetAllCustomers();
    });
  }

  delete(id:number){
    this._cusSer.delete(id).subscribe((data: any) =>{
      console.log(data);
      this.GetAllCustomers();
    });
  }

}

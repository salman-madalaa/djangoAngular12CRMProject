import { Component, OnInit } from '@angular/core';
import { Router, Routes } from '@angular/router';
import { CustomerService } from '../services/customer.service';

@Component({
  selector: 'app-new',
  templateUrl: './new.component.html',
  styleUrls: ['./new.component.css']
})
export class NewComponent implements OnInit {

  customer={
    name:'',
    type:'',
    phone: '',
    address: ''
  }

  constructor(private _cusSer:CustomerService,private router:Router) { }

  ngOnInit(): void {
  }

  create(customer:any){
    console.log(customer);
    this._cusSer.createCustomer(customer).subscribe(data=>{
      console.log(data);
      this.router.navigateByUrl('/customers/all');
    })
  }

}

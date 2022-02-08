import { Component, OnInit } from '@angular/core';
import { CustomerService } from '../services/customer.service';

@Component({
  selector: 'app-all',
  templateUrl: './all.component.html',
  styleUrls: ['./all.component.css']
})
export class AllComponent implements OnInit {
  customers: any;
  constructor(private _cusSer:CustomerService) { }

  ngOnInit(): void {
    this.GetAllCustomers();
  }

  GetAllCustomers(){
    this._cusSer.getallCustomers().subscribe((data: any) =>{
      this.customers = data.customers;
      console.log(data);
    });
  }

}

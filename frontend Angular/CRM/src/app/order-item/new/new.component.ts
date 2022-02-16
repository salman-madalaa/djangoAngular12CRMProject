import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ProductService } from 'src/app/product/services/product.service';
import { OrderItemService } from '../services/order-item.service';

@Component({
  selector: 'app-new',
  templateUrl: './new.component.html',
  styleUrls: ['./new.component.css']
})
export class NewComponent implements OnInit {
  products:any;
  orderItem={
    orderId:'',
    productId:'',
    quality: '',
    itemTotal: '',
  }

  constructor(private _orderItemSer:OrderItemService,private _prodSer:ProductService,private router:Router) { }

  ngOnInit(): void {
    this.getProducts();
  }

  getProducts() {
    this._prodSer.getallProducts().subscribe((data) => {
      this.products = data.products;
    })
  }

  create(orderItem:any){
    console.log(orderItem);
    this._orderItemSer.createOrderItem(orderItem).subscribe(data=>{
      console.log(data);
      this.router.navigateByUrl('/orderItemOrder/all');
    })
  }
  

}

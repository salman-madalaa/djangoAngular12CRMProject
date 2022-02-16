import { Component, OnInit } from '@angular/core';
import { OrderItemService } from '../services/order-item.service';


@Component({
  selector: 'app-all',
  templateUrl: './all.component.html',
  styleUrls: ['./all.component.css']
})
export class AllComponent implements OnInit {
  orderItems: any;
  customers:any;
  edit: boolean = false;
  enableEditIndex = null;

  newOrderItem={
    orderId:'',
    productId:'',
    quality: '',
    itemTotal: '',
  }

  constructor(private _orderItemSer:OrderItemService) { }

  ngOnInit(): void {
    this.GetAllOrderItems();
  }

  GetAllOrderItems(){
    this._orderItemSer.getallOrderItems().subscribe((data: any) =>{
      this.orderItems = data.OrderItems;
      this.customers = data.customers;
      if (this.orderItems != null ){
        this.orderItems.forEach((element:any) => {
          element['isEdit'] = false;
        });
      }
      console.log(data);
    });
  }

  update(ob:any){
    // this.newOrderItem.id = ob.id;
    this.newOrderItem.orderId = ob.orderId;
    this.newOrderItem.productId = ob.productId;
    this.newOrderItem.quality = ob.quality;
    this.newOrderItem.itemTotal = ob.itemTotal;
    ob.isEdit = true;   
  }

  cancel(customer:any) {
    
    customer.isEdit = false;
  
  }

  save(ob:any,id:number) {
    console.log(ob);
    this._orderItemSer.update(ob,id).subscribe((data: any) =>{
      console.log(data);
      this.GetAllOrderItems();
    });
  }

  delete(id:number){
    this._orderItemSer.delete(id).subscribe((data: any) =>{
      console.log(data);
      this.GetAllOrderItems();
    });
  }

}

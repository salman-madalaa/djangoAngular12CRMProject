import { Component, OnInit } from '@angular/core';
import { PageEvent } from '@angular/material/paginator';
import { ProductService } from '../services/product.service';


@Component({
  selector: 'app-all',
  templateUrl: './all.component.html',
  styleUrls: ['./all.component.css']
})
export class AllComponent implements OnInit {
  products: any;
  customers:any;
  edit: boolean = false;
  enableEditIndex = null;

  totalCount:any;

  pageEvent!: PageEvent;

  newProduct={
    units:'',
    name:'',
    price: '',
  }

  pagination = {
    previousPageIndex : 0,
    pageIndex : 0,
    pageSize : 10,
    length : 0
  }
  

  constructor(private _productSer:ProductService) { }

  ngOnInit(): void {
    this.updateTableResults(this.pagination)
     
  }

  GetAllProducts() {
    this._productSer.getallProducts().subscribe((data: any) =>{
      this.products = data.products;
      console.log(this.products.length)
      if (this.products != null ){
        this.products.forEach((element:any) => {
          element['isEdit'] = false;
        });
      }
      console.log(data);
    });
  }

  update(ob:any){
    // this.newProduct.id = ob.id;
    this.newProduct.units = ob.units;
    this.newProduct.name = ob.name;
    this.newProduct.price = ob.price;
    ob.isEdit = true;   
  }

  cancel(customer:any) {
    
    customer.isEdit = false;
  
  }

  save(ob:any,id:number) {
    console.log(ob);
    this._productSer.update(ob,id).subscribe((data: any) =>{
      console.log(data);
      this.GetAllProducts();
    });
  }

  delete(id:number){
    this._productSer.delete(id).subscribe((data: any) =>{
      console.log(data);
      this.GetAllProducts();
    });
  }


  updateTableResults(e:any){
    console.log(e)
    
    this._productSer.getallProductsByPagination(e).subscribe((data: any) =>{
      this.products = data.products;
      this.totalCount = data.totalCount
      if (this.products != null ){
        this.products.forEach((element:any) => {
          element['isEdit'] = false;
        });
      }
      console.log(data);
    });

  }

}

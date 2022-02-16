import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ProductService } from '../services/product.service';

@Component({
  selector: 'app-new',
  templateUrl: './new.component.html',
  styleUrls: ['./new.component.css']
})
export class NewComponent implements OnInit {
  products:any;
  product={
    name:'',
    price: '',
    units:'',
   
  }

  constructor(private _productSer:ProductService,private router:Router) { }

  ngOnInit(): void {
    
  }

  create(product:any){
    console.log(product);
    this._productSer.createProduct(product).subscribe(data=>{
      console.log(data);
      this.router.navigateByUrl('/product/all');
    })
  }
  

}

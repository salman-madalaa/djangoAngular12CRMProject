import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AllComponent } from './all/all.component';
import { NewComponent } from './new/new.component';
import { ProductRoutingModule } from './product-routing.module';
import { FormsModule } from '@angular/forms';
import {MatPaginatorModule} from '@angular/material/paginator';



@NgModule({
  declarations: [
    AllComponent,
    NewComponent
  ],
  imports: [
    CommonModule,
    FormsModule,
    ProductRoutingModule,
    MatPaginatorModule
  ]
})
export class ProductModule { }

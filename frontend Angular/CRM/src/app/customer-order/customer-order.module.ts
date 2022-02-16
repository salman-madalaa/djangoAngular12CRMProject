import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AllComponent } from './all/all.component';
import { NewComponent } from './new/new.component';
import { CustomerOrderRoutingModule } from './customer-order-routing.module';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';



@NgModule({
  declarations: [
    AllComponent,
    NewComponent
  ],
  imports: [
    CommonModule,
    FormsModule,
    CustomerOrderRoutingModule,
    HttpClientModule,
  ]
})
export class CustomerOrderModule { }

import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AllComponent } from './all/all.component';
import { NewComponent } from './new/new.component';
import { CustomerOrderRoutingModule } from './customer-order-routing.module';



@NgModule({
  declarations: [
    AllComponent,
    NewComponent
  ],
  imports: [
    CommonModule,
    CustomerOrderRoutingModule
  ]
})
export class CustomerOrderModule { }

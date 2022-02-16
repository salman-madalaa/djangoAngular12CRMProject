import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AllComponent } from './all/all.component';
import { NewComponent } from './new/new.component';

const routes: Routes = [
  { path: 'all', component: AllComponent },
  { path: 'new', component: NewComponent }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ProductRoutingModule { }

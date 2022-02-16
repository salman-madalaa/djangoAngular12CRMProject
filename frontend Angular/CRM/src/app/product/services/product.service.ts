import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ProductService {

  
  private baseUrl= environment.url;


  constructor(private http:HttpClient) { }

  getallProducts():Observable<any> {
    return this.http.get(this.baseUrl + "product/getAll")
  }

  createProduct(ob:any): Observable<any> {
    let body = JSON.stringify(ob);
    let options = { headers: new HttpHeaders().set('Content-Type', 'application/json') };
    return this.http.post<any>(this.baseUrl + "product/new/",ob)
  }

  update(ob:any,id:number):Observable<any>{
    let body = JSON.stringify(ob);
    let options = { headers: new HttpHeaders().set('Content-Type', 'application/json') };
    return this.http.post<any>(this.baseUrl + "product/update/"+id,ob)
  }

  delete(id:number):Observable<any>{
    return this.http.delete(this.baseUrl + 'product/delete/'+id)
  }

  getallProductsByPagination(ob:any):Observable<any> {
    let body = JSON.stringify(ob);
    let options = { headers: new HttpHeaders().set('Content-Type', 'application/json') };
    console.log(body);
    return this.http.post(this.baseUrl + "product/get/page/",body)
  }

}

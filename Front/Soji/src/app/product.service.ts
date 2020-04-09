import { Injectable } from '@angular/core';
import { Product} from './product';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError, map, tap } from 'rxjs/operators';
@Injectable({
  providedIn: 'root'
})
export class ProductService {
  private productUrl = 'api/products';
  constructor( private http: HttpClient) { }

  getProducts(): Observable<Product[]> {
    return this.http.get<Product[]>(this.productUrl)
      .pipe(catchError(this.handleError<Product[]>('getHeroes', []))
    );
  }
  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {

      // TODO: send the error to remote logging infrastructure
      console.error(error); // log to console instead

      // TODO: better job of transforming error for user consumption

      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }
  getProduct(id: number): Observable<Product> {
    const url = `${this.productUrl}/${id}`;
    return this.http.get<Product>(url).pipe(
      catchError(this.handleError<Product>(`getHero id=${id}`))
    );
  }
  /* GET heroes whose name contains search term */
  searchProducts(term: string): Observable<Product[]> {
    if (!term.trim()) {
      // if not search term, return empty hero array.
      return of([]);
    }
    return this.http.get<Product[]>(`${this.productUrl}/?name=${term}`).pipe(
      catchError(this.handleError<Product[]>('searchHeroes', []))
    );
  }
}

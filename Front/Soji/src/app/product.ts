export interface Product {
  id: number;
  name: string;
  description: string;
  image?: Array<string>;
  price: number;
  sale?: string;
  salePrice?: number;
}

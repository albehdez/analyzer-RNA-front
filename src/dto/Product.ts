class ProductItem {
  item: string
  price: number
  municipality: string
  tendency: number

  constructor(
    item: string,
    price: number,
    coordinates: { lat: number; lng: number },
    municipality: string,
    tendency: number,
  ) {
    this.item = item
    this.price = price
    this.municipality = municipality
    this.tendency = tendency
  }
}

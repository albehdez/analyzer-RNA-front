// // import axios from 'axios'

// interface Producto {
//   id: number
//   nombre: string
//   precio: number
//   descripcion: string
// }

// export class  ProductoService {
//   private apiUrl: string

//   constructor(apiUrl: string) {
//     this.apiUrl = apiUrl
//   }

//   async obtenerTodosProductos(): Promise<Producto[]> {
//     try {
//       const respuesta = await axios.get<Producto[]>(`${this.apiUrl}/words`)
//       return respuesta.data
//     } catch (error) {
//       console.error('Error al obtener productos:', error)
//       throw error
//     }
//   }
// }

// // Uso del servicio

// }

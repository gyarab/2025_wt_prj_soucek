import { createRouter, createWebHistory } from 'vue-router'
import ProductList from '../views/ProductList.vue'
import ProductDetail from '../views/ProductDetail.vue'


const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/', name: 'home', component: ProductList
        },
        {
            path: '/product/:id', name: 'product', component: ProductDetail
        }
    ]
})

export default router
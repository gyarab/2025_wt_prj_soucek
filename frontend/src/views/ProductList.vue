<script setup>
    import { onMounted, ref } from 'vue'

    const products = ref([])

    async function load() {
        const url = new URL('/api/products', window.location.origin)
        const res = await fetch(url)
        if (!res.ok) throw new Error(`HTTP ${res.status}`)
        const data = await res.json()
    console.log(data)
    products.value = data.results
    }

    function selectProduct(product) {
        console.log('Selected product:', product)
    }

    onMounted(load)
</script>

<template>
    <h2>Product List</h2>
    <div v-for="Product in products">
        <h3>{{ Product.name }}</h3>
        <p>{{ Product.description }}</p>
    </div>
    {{ products }}
</template>

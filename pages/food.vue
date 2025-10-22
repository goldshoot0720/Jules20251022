<script setup lang="ts">
const supabase = useSupabaseClient()
const isOpen = ref(false)
const isEditOpen = ref(false)
const selectedFood = ref(null)
const toast = useToast()

const columns = [
  { key: 'name', label: 'Name' },
  { key: 'amount', label: 'Amount' },
  { key: 'price', label: 'Price' },
  { key: 'shop', label: 'Shop' },
  { key: 'todate', label: 'Date' },
  { key: 'actions', label: 'Actions' }
]

const { data: foods, refresh } = await useAsyncData('foods', async () => {
  const { data } = await supabase.from('food').select('*')
  return data
})

const newFood = ref({
  name: '',
  amount: 0,
  price: 0,
  shop: '',
  todate: ''
})

async function addFood() {
  const { data, error } = await supabase.from('food').insert([newFood.value])
  if (error) {
    toast.add({ title: 'Error', description: error.message, color: 'red' })
  } else {
    isOpen.value = false
    refresh()
    toast.add({ title: 'Success', description: 'Food item added.', color: 'green' })
  }
}

function openEditModal(food) {
  selectedFood.value = { ...food }
  isEditOpen.value = true
}

async function updateFood() {
  const { data, error } = await supabase.from('food').update(selectedFood.value).eq('id', selectedFood.value.id)
  if (error) {
    toast.add({ title: 'Error', description: error.message, color: 'red' })
  } else {
    isEditOpen.value = false
    refresh()
    toast.add({ title: 'Success', description: 'Food item updated.', color: 'green' })
  }
}

async function deleteFood(id) {
  if (!confirm('Are you sure you want to delete this item?')) return
  const { data, error } = await supabase.from('food').delete().eq('id', id)
  if (error) {
    toast.add({ title: 'Error', description: error.message, color: 'red' })
  } else {
    refresh()
    toast.add({ title: 'Success', description: 'Food item deleted.', color: 'green' })
  }
}
</script>

<template>
  <UCard>
    <template #header>
      <div class="flex justify-between">
        <h2 class="text-xl font-bold">Food Management</h2>
        <UButton @click="isOpen = true">Add Food</UButton>
      </div>
    </template>

    <UTable :rows="foods" :columns="columns">
      <template #actions-data="{ row }">
        <UButton @click="openEditModal(row)" color="orange" variant="ghost" icon="i-heroicons-pencil-square" />
        <UButton @click="deleteFood(row.id)" color="red" variant="ghost" icon="i-heroicons-trash" />
      </template>
    </UTable>

    <UModal v-model="isOpen">
      <UCard>
        <template #header>
          <h3 class="text-lg font-bold">Add New Food</h3>
        </template>
        <UForm :state="newFood" @submit.prevent="addFood">
          <UFormGroup label="Name" name="name"><UInput v-model="newFood.name" /></UFormGroup>
          <UFormGroup label="Amount" name="amount"><UInput v-model.number="newFood.amount" type="number" /></UFormGroup>
          <UFormGroup label="Price" name="price"><UInput v-model.number="newFood.price" type="number" /></UFormGroup>
          <UFormGroup label="Shop" name="shop"><UInput v-model="newFood.shop" /></UFormGroup>
          <UFormGroup label="Date" name="todate"><UInput v-model="newFood.todate" type="date" /></UFormGroup>
          <UButton type="submit">Save</UButton>
        </UForm>
      </UCard>
    </UModal>

    <UModal v-model="isEditOpen">
      <UCard>
        <template #header>
          <h3 class="text-lg font-bold">Edit Food</h3>
        </template>
        <UForm v-if="selectedFood" :state="selectedFood" @submit.prevent="updateFood">
          <UFormGroup label="Name" name="name"><UInput v-model="selectedFood.name" /></UFormGroup>
          <UFormGroup label="Amount" name="amount"><UInput v-model.number="selectedFood.amount" type="number" /></UFormGroup>
          <UFormGrup label="Price" name="price"><UInput v-model.number="selectedFood.price" type="number" /></UFormGrup>
          <UFormGroup label="Shop" name="shop"><UInput v-model="selectedFood.shop" /></UFormGroup>
          <UFormGroup label="Date" name="todate"><UInput v-model="selectedFood.todate" type="date" /></UFormGroup>
          <UButton type="submit">Update</UButton>
        </UForm>
      </UCard>
    </UModal>
  </UCard>
</template>

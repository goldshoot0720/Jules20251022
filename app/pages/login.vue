<template>
  <div>
    <h1>Login</h1>
    <UButton @click="login">Login with GitHub</UButton>
  </div>
</template>

<script setup lang="ts">
const supabase = useSupabaseClient()

const login = async () => {
  const { error } = await supabase.auth.signInWithOAuth({
    provider: 'github',
  })
  if (error) {
    console.error(error)
  }
}
</script>

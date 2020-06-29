<template>
  <div class="root">
    <q-page class="">
      <div class="row text-center q-pa-lg content-center">
        <div class="col bo text-h3">Mão 1</div>
        <div class="col bo text-h3">Mão 2</div>
      </div>
      <div class="row">
        <div class="col-5 q-pa-sm">
          <div class="row">
            <q-card
              class="my-card col-3 q-ma-sm"
              v-for="(carta, id) in maos.mao1"
              :key="id"
            >
              <q-card-section>
                <div class="text-subtitle2">Carta {{ id + 1 }}</div>
                <div class="text-h6">{{ carta.naipe }} - {{ carta.valor }}</div>
              </q-card-section>

              <q-separator />

              <q-card-actions vertical>
                <q-select
                  v-model="carta.naipe"
                  :options="naipes"
                  label="Naipe"
                />
                <q-select
                  v-model="carta.valor"
                  :options="valores"
                  label="Valor"
                />
              </q-card-actions>
            </q-card>
          </div>
        </div>

        <q-dialog v-model="alert" v-if="!!vencedor">
          <q-card>
            <q-card-section>
              <div class="text-h3"><b>Vencedor: </b>{{ vencedor.title }}</div>
              <div class="text-h5 text-center q-ma-sm">♠♥ {{ vencedor.vencedor['tipo_mao'] }} ♣♦ </div>
              <div class="text-h3 text-center">👏🎉</div>
               <q-separator />
            </q-card-section>

            <q-card-section class="q-pt-none">

            </q-card-section>

            <q-card-actions align="right">
              <q-btn flat label="OK" color="primary" v-close-popup />
            </q-card-actions>
          </q-card>
        </q-dialog>
        <q-btn
          label="Jogar"
          color="negative"
          @click="putMaos()"
          class="text-h4 q-ma-md self-end"
        />
        <!-- <div class="text-h2 q-ma-md self-end">JOGAR</div> -->
        <div class="col-5 q-pa-sm self-end">
          <div class="row justify-end">
            <q-card
              class="my-card col-3 q-ma-sm"
              v-for="(carta, id) in maos.mao2"
              :key="id"
            >
              <q-card-section>
                <div class="text-subtitle2">Carta {{ id + 1 }}</div>
                <div class="text-h6">{{ carta.naipe }} - {{ carta.valor }}</div>
              </q-card-section>

              <q-separator />

              <q-card-actions vertical>
                <q-select
                  v-model="carta.naipe"
                  :options="naipes"
                  label="Naipe"
                />
                <q-select
                  v-model="carta.valor"
                  :options="valores"
                  label="Valor"
                />
              </q-card-actions>
            </q-card>
          </div>
        </div>
      </div>
    </q-page>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "PageIndex",
  data() {
    return {
      maos: {
        mao1: [
          { naipe: "Copas", valor: "10" },
          { naipe: "Copas", valor: "J" },
          { naipe: "Copas", valor: "Q" },
          { naipe: "Copas", valor: "K" },
          { naipe: "Copas", valor: "A" }
        ],
        mao2: [
          { naipe: "Copas", valor: "2" },
          { naipe: "Copas", valor: "3" },
          { naipe: "Copas", valor: "5" },
          { naipe: "Copas", valor: "4" },
          { naipe: "Copas", valor: "6" }
        ]
      },

      alert: false,
      naipes: ["Copas", "Espadas", "Ouros", "Paus"],
      valores: [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"],
      vencedor: null
    };
  },
  computed:{

  }
  methods: {
    putMaos: function() {
      axios.post("http://127.0.0.1:7000/index/", this.maos).then(comics => {
        this.vencedor = comics.data;
        console.log(this.vencedor);
      });
      this.alert = true;
    },
    checkValues: function(){

    }
  }
};
</script>
<style scoped>
.root {
  background: #08a305;
}
.bo {
  /* border: white 1px solid; */
  color: white;
}
</style>

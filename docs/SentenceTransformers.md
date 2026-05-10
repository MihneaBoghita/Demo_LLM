# Sentence Transformers
Noi vrem să facem o schimbare la aplicația noastră. Deoarece avem prea multe produse, ne-am gândit să le sortăm pe categorii predefinite. Totuși, este destul de laborios să adăugăm toate categoriile unui produs în mod manual. Există vreo cale să facem asta automat?
# Problema
Ex: Avem produsul „Tastatură”. Cum facem astfel încât acesta să fie adăugat automat în categoria „Electronice”?
Pentru noi este evident, dar calculatorul nu înțelege „sensul”, ci doar text exact.
O căutare obișnuită (ex: strstr()) nu funcționează dacă termenii nu coincid exact.
# Exemplu
content = "Președintele României este Nicușor Dan"
Query:
"Liderul României"
 Nu va funcționa, deși sensul este similar.
________________________________________
# Soluția: Sentence Transformers
Un Sentence Transformer este un model pre-antrenat care transformă propozițiile în vectori numerici (embeddings) ce reprezintă sensul acestora.
Astfel, putem compara propoziții matematic, nu textual.
________________________________________
# Procesul
Input:
"O zi însorită"
Pași:
1.	Transformerul analizează relațiile dintre cuvinte
2.	Pooling combină informația într-un vector
Output:
Vector (embedding) de 384 / 768 dimensiuni
________________________________________
# Similaritatea (Cosine Similarity)
Folosim cosine similarity pentru a compara doi vectori:
cos(x) = A·B/|A|·|B|
Unde:
•	A · B = produs scalar
•	|A|, |B| = magnitudinea vectorilor
# Interpretare:
•	1 → foarte similare
•	0 → fără legătură
•	-1 → opuse
________________________________________
# Intuiție (simplificată)
Imaginăm un spațiu cu dimensiuni precum:
•	„mâncare”
•	„casă”
# Exemple:
•	„hot dog” → mare pe „mâncare”
•	„școală” → mare pe „casă”
•	„restaurant” → mare pe ambele
 În realitate, vectorii au sute de dimensiuni.
________________________________________
# Concluzie
Prin transformarea textului în vectori, putem compara sensul propozițiilor chiar dacă ele nu sunt identice.
________________________________________
# Implementare (Python)
from sentence_transformers import SentenceTransformer, util
import torch

# Tipuri de tensori:
# Scalar = rang 0
# Vector = rang 1
# Matrice = rang 2

# 1. Model pre-antrenat
model = SentenceTransformer('all-MiniLM-L6-v2')

# 2. Date
documents = [
    "A man is eating a piece of bread.",
    "A modern skyscraper in a busy city.",
    "The library is a quiet place to study.",
    "A delicious hot dog with mustard.",
    "Education is the key to success."
]

# 3. Encode
doc_embeddings = model.encode(documents, convert_to_tensor=True)

# 4. Căutare semantică
def semantic_search(query, top_k=1):
    query_embedding = model.encode(query, convert_to_tensor=True)

    hits = util.semantic_search(query_embedding, doc_embeddings, top_k=top_k)

    print(f"\nQuery: '{query}'")
    for hit in hits[0]:
        idx = hit['corpus_id']
        score = hit['score']
        print(f"-> Match: '{documents[idx]}' (Similarity: {score:.4f})")

# 5. Test
semantic_search("Where can I read books?")
semantic_search("I'm hungry for a snack")


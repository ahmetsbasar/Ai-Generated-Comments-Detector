import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load genuine comments features DataFrame
print("Loading genuine comments features DataFrame...")
genuine_comments_df = pd.read_csv("Final_Featured_Genuine_Comments.csv")
print("Genuine comments features DataFrame loaded successfully.")

# Load generated comments features DataFrame
print("Loading generated comments features DataFrame...")
generated_comments_df = pd.read_csv("Final_Featured_Combined_Comments.csv")
print("Generated comments features DataFrame loaded successfully.")

# Fill NaN values in the "Comment" column of generated comments DataFrame
generated_comments_df['Comment'].fillna("generated_nan_placeholder", inplace=True)

# Now, check the DataFrame again
print(generated_comments_df.head())

# Split genuine comments into training and testing sets
print("Splitting genuine comments into training and testing sets...")
X_genuine = genuine_comments_df.drop(columns=['label'])
y_genuine = genuine_comments_df['label']
X_train_genuine, X_test_genuine, y_train_genuine, y_test_genuine = train_test_split(X_genuine, y_genuine, test_size=0.2, random_state=42)
print("Genuine comments split into training and testing sets.")
print(X_train_genuine.dtypes)


# Split generated comments into training and testing sets
print("Splitting generated comments into training and testing sets...")
X_generated = generated_comments_df.drop(columns=['label'])
y_generated = generated_comments_df['label']
X_train_generated, X_test_generated, y_train_generated, y_test_generated = train_test_split(X_generated, y_generated, test_size=0.2, random_state=42)
print("Generated comments split into training and testing sets.")

print("X_train_genuine:")
print(X_train_genuine.head())
print("Data types of X_train_genuine:")
print(X_train_genuine.dtypes)

print("\ny_train_genuine:")
print(y_train_genuine.head())
print("Data types of y_train_genuine:")
print(y_train_genuine.dtype)

# Train RandomForestClassifier on genuine comments
print("Training RandomForestClassifier on genuine comments...")
rf_genuine = RandomForestClassifier()
rf_genuine.fit(X_train_genuine, y_train_genuine)
print("RandomForestClassifier trained on genuine comments.")

# Train RandomForestClassifier on generated comments
print("Training RandomForestClassifier on generated comments...")
rf_generated = RandomForestClassifier()
rf_generated.fit(X_train_generated, y_train_generated)
print("RandomForestClassifier trained on generated comments.")

# Evaluate models
def evaluate_model(model, X_test, y_test, comment_type):
    # Predictions
    y_pred = model.predict(X_test)
    
    # Accuracy
    accuracy = accuracy_score(y_test, y_pred)
    
    # Precision
    precision = precision_score(y_test, y_pred)
    
    # Recall
    recall = recall_score(y_test, y_pred)
    
    # F1-score
    f1 = f1_score(y_test, y_pred)
    
    # Print metrics
    print("\nMetrics for", comment_type, "Comments:")
    print("Accuracy:", accuracy)
    print("Precision:", precision)
    print("Recall:", recall)
    print("F1-score:", f1)

# Evaluate models on genuine comments
evaluate_model(rf_genuine, X_test_genuine, y_test_genuine, "Genuine")

# Evaluate models on generated comments
evaluate_model(rf_generated, X_test_generated, y_test_generated, "Generated")

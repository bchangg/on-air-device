describe("Visit app", () => {
  it("passes", () => {
    cy.visit("http://localhost:3000/");
  });
});

export {};
